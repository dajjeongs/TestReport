
from TestReport.TestRail.testrail import APIClient
from dotenv import load_dotenv
import os

load_dotenv()
client = APIClient("https://musinsa.testrail.io/")
client.user = os.getenv('TESTRAIL_USER')
client.password = os.getenv('TESTRAIL_PASSWORD')


def get_run(run_id):
    run = client.send_get("get_run/{}".format(run_id))
    #print(run)
    return run


def get_run_name(run):
    run_name = run['name']
    return run_name


def run_total_count(run):
    total_count = run['passed_count'] + run['blocked_count'] + run['untested_count'] + run['retest_count'] + run[
        'failed_count'] + run['custom_status2_count'] + run['custom_status3_count']
    return total_count

def run_passed(run):
    passed_count = run['passed_count']
    passed_rate = round(passed_count / run_total_count(run) * 100)
    passed = "{} passed / pass rate : {}%" .format(passed_count, passed_rate)
    return passed

def run_failed(run):
    failed_count = run['failed_count']
    failed_rate = round(failed_count / run_total_count(run) * 100)
    failed = "Fail rate : {}%" .format(failed_rate)
    return failed


def run_in_progresed(run):
    in_progress_count = run['custom_status4_count']
    in_progress_rate = round(in_progress_count / run_total_count(run) * 100)
    in_progressed = "{} test in progressed / in progress rate : {}%" .format(in_progress_count, in_progress_rate)
    return in_progressed


def run_untested(run):
    untested_count = run['untested_count']
    untested_rate = round(untested_count / run_total_count(run) * 100)
    untested = "Untest rate : {}%" .format(untested_rate)
    return untested

def progress_rate(run):
    progress_count = run_total_count(run) - run['untested_count'] - run['custom_status4_count']
    progress_rate = round(progress_count / run_total_count(run) * 100)
    progressed = "전체 진행률은 {}%입니다." .format(progress_rate)
    return progressed


def run_result(run_id):
    run = get_run(run_id)
    #name = get_run_name(run)
    progressed = progress_rate(run)
    failed = run_failed(run)
    untested = run_untested(run)
    run_results = f"> {progressed}\n  • {failed}\n  • {untested}"
    return run_results

