import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pytest_html import extras
from pytest_html.extras import image


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://ignou.ac.in/'))
       # extra.image(image, mime_type='image/gif', extension='gif')
       # extras.png(image)

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Mobile Automation"
