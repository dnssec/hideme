const puppeteer = require('puppeteer');
const fs = require('fs');

/**
 * Performs a search on a specific website and takes a screenshot of the search results.
 * @param {string} site_key - The key of the website to search on.
 * @param {string} first_name - The first name to search for.
 * @param {string} last_name - The last name to search for.
 * @returns {Promise<void>} - A promise that resolves when the search and screenshot are completed.
 */
async function do_search_and_screenshot(site_key, first_name, last_name) {
    const urlTemplates = {
        // ... [Your existing URL templates] ...
        '411info': 'https://411.info/people/?fn&{first_name}-{last_name}',
        '411': 'https://www.411.com/person-search/{first_name}-{last_name}',
        'AllPeople': 'https://allpeople.com/search?ss={first_name}+{last_name}&ss-e=&ss-p=&ss-i=&where=&industry-auto=&where-auto=',
        'AdvancedBackgroundChecks': 'https://www.advancedbackgroundchecks.com/names/{first_name}-{last_name}',
        'AdvancedPeopleSearch': 'https://www.advanced-people-search.com/people/{first_name}-{last_name}',
        'Anywho': 'https://www.anywho.com/people/{first_name}+{last_name}',
        'Archives': 'https://www.archives.com/search/ancestor/results?FirstName={first_name}&LastName={last_name}&Country=United%20States&RecordSearchType=Unknown',
        'Arrestfacts': 'https://arrestfacts.com/ng/search?fname={first_name}&lname={last_name}&state=&city=&age=&type=&site=',
        'BackgroundAlerts': 'https://www.backgroundalert.com/path/background/ln/1/results?searchbox=simple&SID=POLoxpD_5sLP7XYEyDA8aSqrOkZT8F9_&fn={first_name}&ln={last_name}',
        'BackgroundCheckRun': 'https://backgroundcheck.run/ng/profile/search?fname={first_name}&lname={last_name}',
        'Blockshoppers': 'https://blockshoppers.com/search/?q={first_name}+{last_name}',
        'Calltruth': 'https://www.calltruth.com/people/{first_name}-{last_name}',
        'Centa': 'https://centeda.com/profile/search?fname={first_name}&lname={last_name}&state=&city=&fage=',
        'CheckPeople': 'https://checkpeople.com/landing/people/k1u2r3t4/searching?firstName={first_name}&lastName={last_name}&state=&city=&aid=11&sid=&tid=&hitid=&iv=&obcid=',
        'ClustrMaps': 'https://clustrmaps.com/persons/{first_name}-{last_name}',
        'Classmates': 'https://www.classmates.com/siteui/search/results?q={first_name}%20{last_name}&searchType=all',
        'Councilon': 'https://councilon.com/profile/search?fname={first_name}&lname={last_name}&state=&city=&fage=',
        'Cubib': 'https://cubib.com/search_results.php?fname={first_name}&lname=&{last_name}&locations:all',
        'CyberBackgroundChecks': 'https://www.cyberbackgroundchecks.com/people/{first_name}-{last_name}',
        'Dataveria': 'https://dataveria.com/profile/search?fname={first_name}&lname={last_name}&state=&city=&fage=',
        'FamilyTreeNow': 'https://www.familytreenow.com/search/genealogy/results?first&{first_name}&last=&{last_name}',
        'FastPeople': 'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}',
        'FindPeopleSearch': 'https://www.findpeoplesearch.com/{first_name}+{last_name}/1/16983092709439',
        'Freepeopledirectory': 'https://www.freepeopledirectory.com/name/{first_name}-{last_name}',
        'Gladiknow': 'https://gladiknow.com/index-people-search?fn={first_name}&ln={last_name}&city=&state=&age=&dob=&relatives=&aliases=&phones=&email=&search=',
        'IDcrawl': 'https://idcrawl.com/{first_name}-{last_name}',
        'Intelius': 'https://www.intelius.com/people-search/&{first_name}&-&{last_name}',
        'LocatePeople': 'https://www.locatepeople.org/{first_name}-{last_name}/',
        'NeighborReport': 'https://neighbor.report/{first_name}-{last_name}',
        'Nuwber': 'https://nuwber.com/search?name={first_name}%20{last_name}',
        'OfficialUSA': 'https://www.officialusa.com/names/{first_name}-{last_name}/',
        'Peeplookup': 'https://www.peeplookup.com/people/search?name={first_name}+{last_name}',
        'Peekyou': 'https://www.peekyou.com/{first_name}_{last_name}',
        'PeopleSearchNow': 'https://www.peoplesearchnow.com/person/{first_name}-{last_name}',
        'PeoplebyName': 'https://www.peoplebyname.com/people/{last_name}/{first_name}',
        'PrivateEye': 'https://www.privateeye.com/people/{first_name}+{last_name}',
        'Publicrecordsnow': 'https://www.publicrecordsnow.com/name/{first_name}+{last_name}/',
        'Pub360': 'https://pub360.com/profile/same/{first_name}-{last_name}',
        'Yasni': 'https://www.yasni.com/{first_name}+{last_name}/check+people',
        'ZabaSearch': 'https://www.zabasearch.com/people/{first_name}+{last_name}/',
        // Add all other site templates here
        'RocketReach': 'http://google.com/search?q=site:rocketreach.co+"{first_name}&{last_name}&"',
        'SearchPeopleFree': 'https://www.searchpeoplefree.com/find/{first_name}&-&{last_name}',
        'Social-Searcher': 'https://www.social-searcher.com/search-users/?q6={first_name}&+&{last_name}',
        'Spokeo': 'https://www.spokeo.com/{first_name}&-&{last_name}&?loaded=1',
        'Spytox': 'https://www.spytox.com/people/search?name= {first_name}&+ &{last_name}',
        'TelephoneDictories': 'https://www.telephonedirectories.us/{first_name}-{last_name}',
        'ThatsThem': 'https://thatsthem.com/name/{first_name}-{last_name}',
        'TruePeople': 'https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}',
        'TruthFinder': 'https://www.truthfinder.com/results/?firstName={first_name}&&lastName={last_name}&state=ALL',
        'Webmii': 'https://webmii.com/people?n=%22{first_name}%20{last_name}%22',
        'WhitePages': 'https://www.whitepages.com/name/{first_name}-{last_name}',
        'Yasni': 'https://www.yasni.com/{first_name}+{last_name}/check+people',
        'ZabaSearch': 'https://www.zabasearch.com/people/{first_name}+{last_name}/',
        // Add all other site templates here
        // BEGIN: ed8c6549bwf9
        'Addresses': 'https://www.addresses.com/people/{first_name}+{last_name}',
        'Addresssearch': 'https://www.addresssearch.com/people-search-full-name.php?fn={first_name}&ln={last_name}',
        // END: ed8c6549bwf9
    };

    if (site_key in urlTemplates) {
        const url = urlTemplates[site_key].replace('{first_name}', first_name).replace('{last_name}', last_name);

        try {
            const browser = await puppeteer.launch();
            const page = await browser.newPage();
            await page.goto(url, { waitUntil: 'load' });
            await page.waitForTimeout(2000); // Adjust the time as needed for the page to load

            await page.screenshot({ path: `${site_key}_${first_name}_${last_name}.png` });

            await browser.close();
        } catch (error) {
            console.error(`An error occurred while accessing ${url}: ${error}`);
        }

    } else {
        console.error(`No URL template found for site key: ${site_key}`);
    }
}

async function do_all_with_screenshots(first_name, last_name) {
    const site_keys = [
    '411info',
    '411',
    'Addresses',
    'Addresssearch',
    'AllPeople',
    'AdvancedBackgroundChecks',
    'AdvancedPeopleSearch',
    'Anywho',
    'Arrestfacts',
    'Archives',
    'BackgroundAlerts',
    'BackgroundCheckRun',
    'Centeda',
    'CheckPeople',
    'ClustrMaps',
    'Classmates',
    'Councilon',
    'Cubib',
    'CyberBackgroundChecks',
    'Dataveria',
    '411info',
    '411',
    'Addresses',
    'Addresssearch',
    'AllPeople',
    'AdvancedBackgroundChecks',
    'AdvancedPeopleSearch',
    'Anywho',
    'Arrestfacts',
    'LocatePeople',
    'NeighborReport',
    'Nuwber',
    'OfficialUSA',
    'Peeplookup',
    'Peekyou',
    'PeopleSearchNow',
    'PeoplebyName',
    'PrivateEye',
    'Publicrecordsnow',
    'Pub360',
    'RocketReach',
    'SearchPeopleFree',
    'Social-Searcher',
    'Spokeo',
    'Spytox',
    'TelephoneDictories',
    'ThatsThem',
    'TruePeople',
    'TruthFinder',
    'Webmii',
    'WhitePages',
    'Yasni',
    'ZabaSearch',
    ];

    for (const site_key of site_keys) {
        await do_search_and_screenshot(site_key, first_name, last_name);
    }
}

// Example usage:
do_all_with_screenshots("John", "Doe");

