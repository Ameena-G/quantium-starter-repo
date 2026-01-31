from dash.testing.application_runners import import_app
from dash import html, dcc


def get_all_components(component):
    components = [component]

    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            for child in children:
                components.extend(get_all_components(child))
        elif children is not None:
            components.extend(get_all_components(children))

    return components


def test_header_present():
    app = import_app("app")
    components = get_all_components(app.layout)

    headers = [c for c in components if isinstance(c, html.H1)]
    assert len(headers) > 0
    assert "Pink Morsel" in headers[0].children


def test_visualisation_present():
    app = import_app("app")
    components = get_all_components(app.layout)

    graphs = [
        c for c in components
        if isinstance(c, dcc.Graph) and c.id == "sales-line-chart"
    ]
    assert len(graphs) == 1


def test_region_picker_present():
    app = import_app("app")
    components = get_all_components(app.layout)

    radios = [
        c for c in components
        if isinstance(c, dcc.RadioItems) and c.id == "region-selector"
    ]
    assert len(radios) == 1
