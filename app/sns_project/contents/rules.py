import rules

# Predicates
@rules.predicate
def is_group_A():
    return rules.is_group_member( 'group_A' )