import json
from test_base import slash


def parse_protractor_test_report(filename):
    print('Checking Protractor test result in: {}\n'.format(filename))
    with open('C:{0}users{0}nick.hartley{0}desktop{0}auto{0}'
              'protractor_tests{0}reports{0}json{0}{1}'.format(slash, filename)) as lines:
        obj = json.load(lines)
        steps = obj[0]['elements'][0]['steps']

    line = 'Checking result for test: {}'.format(obj[0]['elements'][0]['name'])
    print(line)

    for step in steps:
        result = step['result']['status']
        name = step['name']
        line = '    {} - {}'.format(name, result)
        print(line)
        assert result.lower() == 'passed', 'Protractor test failure.\n    Step: {}\n    Result: {}\n'.format(name, result)
    print('\nProtractor test was successful...\n')


'''
def parse_protractor_test_report():
    # Creating a dictionary from new_report.json
    with open('C:{0}users{0}nick.hartley{0}desktop{0}auto{0}'
              'protractor_tests{0}reports{0}json{0}new_report.json'.format(slash), 'r') as lines:
        obj = json.load(lines)
        tests = obj[0]['elements'][0]['steps']

    check = False

    for test in tests:
        result = test['result']['status']
        print(test['name'], result)

        if result == 'passed':
            check = True
        elif result == 'failed':
            check = False
            print(test['result']['error_message'])
        else:
            check = False

    print(check)
    return check
'''
