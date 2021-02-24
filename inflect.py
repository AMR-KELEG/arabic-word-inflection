def inflect_verb(verb_stem):
    prefixes = ['ا', 'ي', 'ت', 'ن', 'ه', 'سا', '']
    suffixes = ['ني', 'ك', 'ها', 'هم', 'كم', 'هن', 'نا', '']
    pre_prefixes = ['و', '', 'ف']
    return sorted(['{}{}{}{}'.format(pp, pre, verb_stem, suf) if not verb.startswith('ا')
            else '{}{}{}{}'.format(pp, pre, verb_stem[1:], suf)
            for pp in pre_prefixes
            for suf in suffixes
            for pre in prefixes])

def inflect_noun(noun):
    prefixes = ['ال', 'بال', 'عال', 'لل', '']
    pre_prefixes = ['و', '', 'ف']
    return ['{}{}{}'.format(pp, p, noun)
            for pp in pre_prefixes
            for p in prefixes]

