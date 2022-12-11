from firewall_api import get_firewall_rules, change_firewall_rule


def turn_on_all():
    rules = get_firewall_rules()
    for rule in rules:
        change_firewall_rule(rule['uuid'], state=1)


if __name__ == '__main__':
    turn_on_all()
