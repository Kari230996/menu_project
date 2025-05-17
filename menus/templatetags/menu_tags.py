from django import template
from django.urls import reverse, NoReverseMatch
from menus.models import MenuItem
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_path = context["request"].path
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name).select_related("parent")

    tree = build_menu_tree(menu_items)
    active_branch = find_active_branch(tree, current_path)

    html = render_menu(tree, active_branch)
    return mark_safe(html)


def build_menu_tree(menu_items):
    tree = {}
    lookup = {}

    for item in menu_items:
        lookup[item.id] = {"item": item, "children": []}

    for item_dict in lookup.values():
        item = item_dict["item"]
        if item.parent_id:
            lookup[item.parent_id]["children"].append(item_dict)
        else:
            tree[item.id] = item_dict

    return tree


def find_active_branch(tree, current_path):
    def match(node):
        item = node["item"]
        try:
            url = item.url or reverse(item.named_url)
        except NoReverseMatch:
            url = item.url
        return url == current_path

    def dfs(node):
        if match(node):
            return [node["item"].id]
        for child in node["children"]:
            result = dfs(child)
            if result:
                return [node["item"].id] + result
        return []

    active = []
    for node in tree.values():
        result = dfs(node)
        if result:
            active = result
            break
    return set(active)


def render_menu(tree, active_branch):
    def render_node(node):
        item = node['item']
        children = node['children']
        is_active = item.id in active_branch
        try:
            url = item.url or reverse(item.named_url)
        except NoReverseMatch:
            url = item.url

        li_class = 'active' if is_active else ''
        html = f'<li class="{li_class}"><a href="{url}">{item.title}</a>'
        if children and is_active:
            html += '<ul>'
            for child in children:
                html += render_node(child)
            html += '</ul>'
        html += '</li>'
        return html

    html = '<ul>'
    for node in tree.values():
        html += render_node(node)
    html += '</ul>'
    return html
