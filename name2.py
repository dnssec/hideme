import webbrowser

def do_pop_all(first_name, last_name):
    # This function would populate all fields, but in a headless environment, it's not applicable.
    print(f"Populating all fields with First Name: {first_name}, Last Name: {last_name}")

def do_search(site_key, first_name, last_name):
    url_templates = {
        'TruePeople': 'https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}',
        'FastPeople': 'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}',
        'Nuwber': 'https://nuwber.com/search?name={first_name}%20{last_name}',
        'XLEK': 'https://xlek.com/search_results.php?fname={first_name}&lname={last_name}&locations:all',
        'Cubib': 'https://cubib.com/search_results.php?fname={first_name}&lname=&{last_name}&locations:all',
        'FamilyTreeNow': 'https://www.familytreenow.com/search/genealogy/results?first&{first_name}&last=&{last_name}',
        'Intelius': 'https://www.intelius.com/people-search/&{first_name}&-&{last_name}',
        'Radaris': 'https://radaris.com/p/{first_name}&/&{last_name}',
        'CyberBackgroundChecks': 'https://www.cyberbackgroundchecks.com/people/{first_name}&-&{last_name}',
        'Spytox': 'https://www.spytox.com/people/search?name= {first_name}&+ &{last_name}',
        'SearchPeopleFree': 'https://www.searchpeoplefree.com/find/{first_name}&-&{last_name}',
        'Spokeo': 'https://www.spokeo.com/{first_name}&-&{last_name}&?loaded=1',
        'AdvancedBackgroundChecks': 'https://www.advancedbackgroundchecks.com/names/{first_name}-{last_name}', 
        'Yasni': 'https://www.yasni.com/{first_name}+{last_name}/check+people',
        'ZabaSearch': 'https://www.zabasearch.com/people/{first_name}+{last_name}/',
        'PeopleSearchNow': 'https://www.peoplesearchnow.com/person/{first_name}-{last_name}',
        'Webmii': 'https://webmii.com/people?n=%22{first_name}%20{last_name}%22',
        'Social-Searcher': 'https://www.social-searcher.com/search-users/?q6={first_name}&+&{last_name}',
        'TruthFinder': 'https://www.truthfinder.com/results/?firstName={first_name}&&lastName={last_name}&state=ALL',
        'PeoplebyName': 'https://www.peoplebyname.com/people/{last_name}/{first_name}',
        'WhitePages': 'https://www.whitepages.com/name/{first_name}-{last_name}',
        'ThatsThem': 'https://thatsthem.com/name/{first_name}-{last_name}',
        'ClustrMaps': 'https://clustrmaps.com/persons/{first_name}-{last_name}',
        'RocketReach': 'http://google.com/search?q=site:rocketreach.co+"{first_name}&{last_name}&"',
        'OfficialUSA': 'https://www.officialusa.com/names/{first_name}-{last_name}/',
        'Classmates': 'https://www.classmates.com/siteui/search/results?q={first_name}%20{last_name}&searchType=all',
        'IDcrawl': 'https://idcrawl.com/{first_name}-{last_name}',
        # Add all other site templates here
    }
    
    url = url_templates.get(site_key).format(first_name=first_name, last_name=last_name)
    webbrowser.open(url, new=2)

def do_all(first_name, last_name):
    site_keys = [
        'TruePeople',
        'FastPeople',
        'Nuwber',
        'XLEK',
        'Cubib',
        'FamilyTreeNow',
        'Intelius',
        'Radaris',
        'CyberBackgroundChecks',
        'Spytox',
        'SearchPeopleFree',
        'Spokeo',
        'AdvancedBackgroundChecks',
        'Yasni',
        'ZabaSearch',
        'PeopleSearchNow',
        'Webmii',
        'Social-Searcher',
        'TruthFinder',
        'PeoplebyName',
        'WhitePages',
        'ThatsThem',
        'ClustrMaps',
        'RocketReach',
        'OfficialUSA',
        'Classmates',
        'IDcrawl',
        # Add all other site keys here
    ]
    
    for site_key in site_keys:
        do_search(site_key, first_name, last_name)

# Example usage:

# Simulating the form submission for doPopAll
do_pop_all("John", "Doe")

# Simulating individual form submissions
do_search("TruePeople", "John", "Doe")
do_search("FastPeople", "John", "Doe")

# Simulating 'Submit All' button
do_all("John", "Doe")

