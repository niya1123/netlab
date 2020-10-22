import rules

@rules.predicate
def is_provider_member(user):
    features = rules.RuleSet()
    features.add_rule('is_provider_member', rules.is_group_member('provider'))
    return features.test_rule('is_provider_member', user)

rules.add_perm('contents.rules_manage_content', is_provider_member)