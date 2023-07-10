from TestReport.TestRail.testrail import APIClient

client = APIClient("https://musinsa.testrail.io/")
client.user = "dajjeong@29cm.co.kr"
client.password = "lee0OCpd0yoHtU1Co62B-NcipdPFVfli4m3EUsArI"


def get_case(case_id):
    case = client.send_get("get_case/{}" .format(case_id))
    return case


def get_plan(plan_id):
    plan = client.send_get("get_plan/{}" .format(plan_id))
    print(plan)
    return plan


def get_name(plan):
    test_name = plan['name']
    return test_name


def get_total_count(plan):
    total_count = plan['passed_count'] + plan['blocked_count'] + plan['untested_count'] + plan['retest_count'] + plan[
        'failed_count'] + plan['custom_status3_count']
    return total_count


def passed_rate(plan):
    passed_rate = plan['passed_count'] / get_total_count(plan) * 100
    return round(passed_rate)


def failed_rate(plan):
    failed_rate = plan['failed_count'] / get_total_count(plan) * 100
    return round(failed_rate)


def untested_rate(plan):
    untested_rate = plan['untested_count'] / get_total_count(plan) * 100
    return round(untested_rate)

def test_inprogress_rate(plan):
    test_inprogress = plan['custom_status3_count'] / get_total_count(plan) * 100
    return round(test_inprogress)


def plan_result(plan_id):
    plan = get_plan(plan_id)
    pass_rate = "Passed Rate : {}%" .format(passed_rate(plan))
    fail_rate = "Failed Rate : {}%" .format(failed_rate(plan))
    untest_rate = "Untested Rate : {}%" .format(untested_rate(plan))
    inprogress_rate = "In Progress Rate : {}%" .format(test_inprogress_rate(plan))
    testrail_result = "- {} \n - {} \n - {}\n - {}" .format(pass_rate, fail_rate, untest_rate, inprogress_rate)
    # print(testrail_result)
    return testrail_result




