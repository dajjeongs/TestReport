
from TestReport.TestRail.testrail import APIClient
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt

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
        'failed_count'] + run['custom_status2_count'] + run['custom_status4_count']
    return total_count


def run_passed(run):
    passed_count = run['passed_count']
    # passed_rate = round(passed_count / run_total_count(run) * 100)
    # passed = "{} passed / pass rate : {}%" .format(passed_count, passed_rate)
    return passed_count


def run_failed(run):
    failed_count = run['failed_count']
    # failed_rate = round(failed_count / run_total_count(run) * 100)
    # failed = "Fail rate : {}%" .format(failed_rate)
    return failed_count


def run_in_progresed(run):
    in_progressed_count = run['custom_status4_count']
    # in_progress_rate = round(in_progress_count / run_total_count(run) * 100)
    # in_progressed = "{} test in progressed / in progress rate : {}%" .format(in_progress_count, in_progress_rate)
    return in_progressed_count


def run_untested(run):
    untested_count = run['untested_count']
    # untested_rate = round(untested_count / run_total_count(run) * 100)
    # untested = "Untest rate : {}%" .format(untested_rate)
    return untested_count

def run_na(run):
    na_count = run['custom_status2_count']
    return na_count

def progress_rate(run):
    progress_count = run_total_count(run) - run['untested_count'] - run['custom_status4_count']
    progress_rate = round(progress_count / run_total_count(run) * 100)
    progressed = "전체 진행률은 {}%입니다." .format(progress_rate)
    return progressed


def run_result(run_id):
    run = get_run(run_id)

    progressed = progress_rate(run)

    passed_count = run_passed(run)
    passed_rate = round(passed_count / run_total_count(run) * 100)
    passed = "{} passed / pass rate : {}%" .format(passed_count, passed_rate)

    failed_count = run_failed(run)
    failed_rate = round(failed_count / run_total_count(run) * 100)
    failed = "Fail rate : {}%".format(failed_rate)

    run_results = f"> {progressed}\n  • {passed}\n  • {failed}"

    print(run_results)

    return run_results


def run_bar_chart(run_id):
    run = get_run(run_id)
    total_count = run_total_count(run)

    passed_count = run_passed(run)

    failed_count = run_failed(run)

    untested_count = run_untested(run) + run_in_progresed(run)

    na_count = run_na(run)

    labels = ["total", "pass", 'fail', "untest", 'n/a']
    count = [total_count, passed_count, failed_count, untested_count, na_count]

    plt.figure(figsize=[4, 4])
    plt.title('Test Progress Rate')
    bar = plt.bar(labels, count, color=['#669966', '#80afe5', '#ff9999', '#CCCCCC', '#FFCC66'], width=0.4)

    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha='center', va='bottom', size=10)

    plt.savefig(f'chart.png')
    plt.show()

def run_pie_chart(run_id):
    run = get_run(run_id)
    print(run)
    total_count = run_total_count(run)

    passed_count = run_passed(run)

    failed_count = run_failed(run)

    untested_count = run_untested(run) + run_in_progresed(run)

    na_count = run_na(run)

    labels = [f'pass/{passed_count}', f'fail/{failed_count}', f'untest/{untested_count}', f'N/A/{na_count}']
    count = [passed_count, failed_count, untested_count, na_count]
    color = ['#80afe5', '#ff9999', '#CCCCCC', '#FFCC66']
    explode = [0.05, 0.05, 0, 0]

    plt.figure(figsize=[4, 4])
    plt.pie(count, labels=labels, autopct='%.1f%%', colors=color, explode=explode)
    plt.title(f'TOTAL COUNT : {total_count}', fontsize=12)
    plt.show()


# run_result(493)
# run_pie_chart(493)
# run_bar_chart(493)




