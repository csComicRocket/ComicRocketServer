/* Base page structure */
body {
    margin:0;
    padding:0 0 20px;
    background-image:url('/img/ghost-tile.gif');
    font-family:"Verdana",sans-serif;
    text-align:center;
    color:#FFFFFF;
}
#bodywrap {
    position:relative;
    background-color:transparent;
    margin:0 auto;
    padding:0 20px;
    width:900px; /* Comment out this line (put /* at the beginning) if you want a fluid-width website) */
    text-align:left;
}




/* Some defaults you can play around with */
a {
    color:#CCCCCC;
text-decoration:none;
}
a:visited {
    color:#CCCCCC;
text-decoration:none;
}
a:hover, a:active {
    color:#FFFFFF !important;
text-decoration: none;
}
h1 a, h2 a, h3 a, h4 a {text-decoration:none;}
h1 a {color:#444 !important;}
h2 a {color:#000 !important;}

a img {border:none 0px;}
p {
    font-family: "Verdana", sans-serif;
}




/* Header */
h1 {
    margin:10px 0 5px;
    padding:20px 0 0;
    text-align:center;
width: 100% !important;
height: 131px !important;
align: center;
}

h1 a {
}

#topnav {
    margin:0 0 1em;
    text-align:center;
}
#topnav a {
    padding:0 10px;
    text-decoration:none;
    font-size:16px;
    font-weight:bold;
    letter-spacing:0.2em;
    font-variant:small-caps;
    border-top: 0px;
    border-bottom: 0px;
}
#topnav a:hover {
    color:#00d;
}





/* Comics! */
#dropdownform {
    float:right;
    margin:10px 0 0;
    padding:5px;
    
    font-size:14px;
    background-color:#171717;
    color:#fff;
}
.navbar {
    display:block;
    padding:5px;
    
    text-align:center;
    color:#bbb;
    background-color:#171717;
    letter-spacing:0.2em;
}
.navbar a {
    text-decoration:none;
    color:#fff;
    font-weight:bold;
}
.navbar a:visited {
    color:#ddd;
}
.navbar a:hover {
    color:#fff;
}
#comicset {
    display:block;
    clear:both;
    margin:15px 0px 20px 0px;
    
    text-align:center;
    background-color:#171717;
    
}
#comicset h2 {border:none 0px;}
#comicimg {
    margin:10px 0;
}
#comicblurb {
font-size:12px;
    margin:20px;
    padding:0 10px 10px;
    border: 0px;
}



/* News! */
.newspost {
    margin:1em 0 4em;
    background-color:transparent;
}
.newspost p {
    font-size:12px;

}
.newsdetail {
    float:right;
    text-align:right;
    margin:0 0 10px 10px;
    padding:0 10px;
    font-size:12px;
    color:#888888;
    border-left:solid 3px #555555;
    background-color:transparent;
}
.newsavatar {float:right;}
.newslinks {
    border-top:dashed 1px #888;
}
.newslinks a {text-decoration:none;}

/* Comments */
 #comments { color:#e1e1e1; font-family:"Verdana",sans-serif; margin: 5px; font-size: 12px; background-color: ##171717; border: solid 1px #666666;}

.commentavatar {float: left; margin: 0 5px 0 0;}

.commentdetail {font-size: 9px; margin: 0px 5px 0px 5px; padding: 0;}

#comments p { color: #FFFFFF; clear:both; margin: 15px 15px 20px 50px; border: solid #555555 0px 0px 1px 0px;}


@param string $email The email address

@param string $s Size in pixels, defaults to 80px [ 1 - 2048 ]

@param string $d Default imageset to use [ 404 | mm | identicon | monsterid | wavatar ]

@param string $r Maximum rating (inclusive) [ g | pg | r | x ]

@param boole $img True to return a complete IMG tag False for just the URL

@param array $atts Optional, additional key/value attributes to include in the IMG tag

@return String containing either just a URL or a complete image tag

@source http://gravatar.com/site/implement/images/php/

 */

function get_gravatar( $email, $s = 80, $d = 'mm', $r = 'g', $img = false, $atts = array() ) {

    $url = 'http://www.gravatar.com/avatar/';

    $url .= md5( strtolower( trim( $email ) ) );

    $url .= "?s=$s&d=$d&r=$r";

    if ( $img ) {

        $url = '<img src="' . $url . '"';

        foreach ( $atts as $key => $val )

            $url .= ' ' . $key . '="' . $val . '"';

        $url .= ' />';

    }

    return $url;

}




/* General content */
h2 {
    margin:20px 0 5px;
    padding:0 20px;
    border-bottom:solid 1px #444;
}
h3 {
    color:#666;
    padding:0 5px;
    font-size:1.2em;
    line-height:1.4em;
    font-variant:small-caps;
    letter-spacing:0.3em;
    background-color:#171717;
}
#maincontent {
    padding:0 10px 10px;
    background-color:transparent;
}



/* Extra content */
#sidenav {
    float:right;
    width:200px;
    font-size:11px;
}
#mainlower {
    padding:10px 260px 0 0;
}
#sidenav h3 {
    border:solid 1px #444;
    background-color:transparent;
}