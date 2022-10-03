def inflect_verb(verb_stem):
    prefixes = ['ا', 'ي', 'ت', 'ن', 'ه', 'سا', '']
    suffixes = ['ني', 'ك', 'ها', 'هم', 'كم', 'هن', 'نا', '']
    pre_prefixes = ['و', '', 'ف']
    return sorted(['{}{}{}{}'.format(pp, pre, verb_stem, suf) if not verb.startswith('ا')
            else '{}{}{}{}'.format(pp, pre, verb_stem[1:], suf)
            for pp in pre_prefixes
            for suf in suffixes
            for pre in prefixes
        ]
    )


def inflect_verb_egy(verb_stem):
    inflections = []
    # Past:
    ## 1st sg masc/fem - 2nd sg masc
    inflections.append(f"{verb_stem}ت")
    ## 1st pl
    inflections.append(f"{verb_stem}نا")
    ## 2nd sg fem
    inflections.append(f"{verb_stem}تي")
    ## 2nd pl
    inflections.append(f"{verb_stem}توا")
    ## 3rd sg masc
    inflections.append(f"{verb_stem}")
    ## 3rd sg fem
    # TODO: Handle Yaa
    if verb_stem[-1] in "يى":
        inflections.append(f"{verb_stem[:-1]}ت")
    else:
        inflections.append(f"{verb_stem}ت")
    ## 3rd pl
    # TODO: Handle Yaa
    if verb_stem[-1] in "يى":
        inflections.append(f"{verb_stem[:-1]}وا")
    else:
        inflections.append(f"{verb_stem}وا")

    print(inflections)
    #  Present

    # Imperative

    return inflections


def inflect_noun(noun):
    prefixes = ['ال', 'بال', 'عال', 'لل', '']
    pre_prefixes = ['و', '', 'ف']
    return ['{}{}{}'.format(pp, p, noun)
            for pp in pre_prefixes
            for p in prefixes]

