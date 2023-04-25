MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

notIncluded = ["<", ">", "/html", "/div", "/body",
               "{", "}", ":", "''", "scriptLoader",
               "[", "]", "true", "appGip", ",",
               "false", "id", "tab", "/", "shortName",
               "``", "div", "by-round", "isFallback", "gssp",
               "customServer", "id=", "/script", "slug", "buildId",
               "modal-root", "name", "...", "page", "isMobile", "/leagues/",
               ";", "@", "null", "ssr", "/match/", "--", "/span",
               "/footer", "--", "!", "class=", "https", "(", ")", "meta", "content=",
               "title", "/title", ".", "DOCTYPE", "html", "en", "head", "name=",
               "href=", "property=", "charset=", "?", "lang=", "link", "rel=", "fb",
               "script", "defer=", "src="]

SEASONS = {
    1 : ["2023", "2022", "2021"],
    2 : ["2022-2023", "2021-2022", "2020-2021", "2019-2020"]
}

SEASON = {
     1 : ["2023", "2022", "2021", "2020", "2019", "2018", "2017",
         "2016", "2015", "2014", "2013", "2012", "2011"],
     2 : ["2022-2023", "2021-2022", "2020-2021", "2019-2020", "2018-2019", "2017-2018",
         "2016-2017", "2015-2016", "2014-2015", "2013-2014", "2012-2013", "2011-2012"]
}
