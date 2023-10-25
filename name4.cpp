// Author @brokep / x.com/prolifichacker
#include <iostream>
#include <string>
#include <unordered_map>
#include <cstdlib>  // for std::system

void do_pop_all(const std::string& first_name, const std::string& last_name) {
    std::cout << "Populating all fields with First Name: " << first_name << ", Last Name: " << last_name << std::endl;
}

void do_search(const std::string& site_key, const std::string& first_name, const std::string& last_name) {
    std::unordered_map<std::string, std::string> url_templates = {
        {"411", "xdg-open 'https://www.411.com/person-search/" + first_name + "-" + last_name + "'"},
        {"411info", "xdg-open 'https://411.info/people/?fn=" + first_name + "&ln=" + last_name + "'"},
        {"Addresses", "xdg-open 'https://www.addresses.com/people/" + first_name + "+" + last_name + "'"},
        {"Addresssearch", "xdg-open 'https://www.addresssearch.com/people-search-full-name.php?fn=" + first_name + "&ln=" + last_name + "'"},
        {"AdvancedBackgroundChecks", "xdg-open 'https://www.advancedbackgroundchecks.com/names/" + first_name + "-" + last_name + "'"},
        {"AdvancedPeopleSearch", "xdg-open 'https://www.advanced-people-search.com/people/" + first_name + "-" + last_name + "'"},
        {"ClustrMaps", "xdg-open 'https://clustrmaps.com/persons/" + first_name + "-" + last_name + "'"},
        {"Classmates", "xdg-open 'https://www.classmates.com/siteui/search/results?q=" + first_name + "%20" + last_name + "&searchType=all'"},
        {"Cubib", "xdg-open 'https://cubib.com/search_results.php?fname=" + first_name + "&lname=" + last_name + "&locations:all'"},
        {"CyberBackgroundChecks", "xdg-open 'https://www.cyberbackgroundchecks.com/people/" + first_name + "-" + last_name + "'"},
        {"FamilyTreeNow", "xdg-open 'https://www.familytreenow.com/search/genealogy/results?first=" + first_name + "&last=" + last_name + "'"},
        {"FastPeople", "xdg-open 'https://www.fastpeoplesearch.com/name/" + first_name + "-" + last_name + "'"},
        {"IDcrawl", "xdg-open 'https://idcrawl.com/" + first_name + "-" + last_name + "'"},
        {"Intelius", "xdg-open 'https://www.intelius.com/people-search/" + first_name + "-" + last_name + "'"},
        {"Nuwber", "xdg-open 'https://nuwber.com/search?name=" + first_name + "%20" + last_name + "'"},
        {"OfficialUSA", "xdg-open 'https://www.officialusa.com/names/" + first_name + "-" + last_name + "/'"},
        {"PeopleSearchNow", "xdg-open 'https://www.peoplesearchnow.com/person/" + first_name + "-" + last_name + "'"},
        {"PeoplebyName", "xdg-open 'https://www.peoplebyname.com/people/" + last_name + "/" + first_name + "'"},
        {"Radaris", "xdg-open 'https://radaris.com/p/" + first_name + "/" + last_name + "'"},
        {"RocketReach", "xdg-open 'http://google.com/search?q=site:rocketreach.co+\"" + first_name + " " + last_name + "\"'"},
        {"SearchPeopleFree", "xdg-open 'https://www.searchpeoplefree.com/find/" + first_name + "-" + last_name + "'"},
        {"Social-Searcher", "xdg-open 'https://www.social-searcher.com/search-users/?q=" + first_name + "+" + last_name + "'"},
        {"Spokeo", "xdg-open 'https://www.spokeo.com/" + first_name + "-" + last_name + "?loaded=1'"},
        {"Spytox", "xdg-open 'https://www.spytox.com/people/search?name=" + first_name + "+" + last_name + "'"},
        {"ThatsThem", "xdg-open 'https://thatsthem.com/name/" + first_name + "-" + last_name + "'"},
        {"TruePeople", "xdg-open 'https://www.truepeoplesearch.com/results?name=" + first_name + "%20" + last_name + "'"},
        {"TruthFinder", "xdg-open 'https://www.truthfinder.com/results/?firstName=" + first_name + "&lastName=" + last_name + "&state=ALL'"},
        {"Webmii", "xdg-open 'https://webmii.com/people?n=%22" + first_name + "%20" + last_name + "%22'"},
        {"WhitePages", "xdg-open 'https://www.whitepages.com/name/" + first_name + "-" + last_name + "'"},
        {"Yasni", "xdg-open 'https://www.yasni.com/" + first_name + "+" + last_name + "/check+people'"},
        {"ZabaSearch", "xdg-open 'https://www.zabasearch.com/people/" + first_name + "+" + last_name + "/'"},
        // add all other site templates here
    };

    std::string command = url_templates[site_key];
    std::system(command.c_str());
}

void do_all(const std::string& first_name, const std::string& last_name) {
    std::string site_keys[] = {
        "411",
        "411info",
        "Addresses",
        "Addresssearch",
        "AdvancedBackgroundChecks",
        "AdvancedPeopleSearch",
        "ClustrMaps",
        "Classmates",
        "Cubib",
        "CyberBackgroundChecks",
        "FamilyTreeNow",
        "FastPeople",
        "IDcrawl",
        "Intelius",
        "Nuwber",
        "OfficialUSA",
        "PeopleSearchNow",
        "PeoplebyName",
        "Radaris",
        "RocketReach",
        "SearchPeopleFree",
        "Social-Searcher",
        "Spokeo",
        "Spytox",
        "ThatsThem",
        "TruePeople",
        "TruthFinder",
        "Webmii",
        "WhitePages",
        "Yasni",
        "ZabaSearch"
        // add all other site keys here
	// more to be added from workbook
    };

    for(const auto& site_key : site_keys) {
        do_search(site_key, first_name, last_name);
    }
}

int main() {
    // Example usage
    do_pop_all("John", "Doe");
    do_search("411", "John", "Doe");
    do_all("John", "Doe");

    return 0;
}
