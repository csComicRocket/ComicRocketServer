-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 14, 2013 at 04:19 AM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `crts`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE IF NOT EXISTS `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `datetime` datetime DEFAULT NULL,
  `username` varchar(64) NOT NULL,
  `title` text NOT NULL,
  `body` text NOT NULL,
  `avatar` text NOT NULL COMMENT 'path to avatar (relative to page''s webroot)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `components`
--

CREATE TABLE IF NOT EXISTS `components` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(64) NOT NULL,
  `value` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=71 ;

--
-- Dumping data for table `components`
--

INSERT INTO `components` (`id`, `key`, `value`) VALUES
(1, 'title', 'Quia Uviysl'),
(2, 'hover', 'Ieklukqu uessak tzjumstai ripsiam eezuistaigh oozea hiepn iehoughuih. Yiriac waiseeshei mueng mee oiaslss aiveapno aklyghai iwi aeheickuep. Hack aewith klych mia ssea azaikae.'),
(8, 'hover', 'Sttzgheichog uickquuishaec uimeattee xoukqu eiqu daiziui.'),
(5, 'title', 'Psysee Ymytz Ngeefekl Foaij Eeghaexeista'),
(6, 'hover', 'Osheesouz oucku ui shouchookl o eapnottgae kex. Geh pseshieckae iekzghiagh slytie othaestea cuismysh iru.'),
(7, 'title', 'Klueufsl Keepuntz'),
(9, 'title', 'Eazousschshei Ocgoo Aissyquk Ia'),
(10, 'hover', 'Iekar ssiavee ngojyxie ver pnooz oogiagqu xattfia ngop yvo uistaesla tzopei uwyvawei. Uimui aiuiba edez ybu cheingae iakocku psuinguej iefoochueth tzoodumopni kr. Iaxea aemeatztze vuuist knuttea ichus hjeastuez desiajear oostee sluixu wouttur uessaith aengops zaixich.'),
(11, 'title', 'Rieno Ossai Kkyeer'),
(12, 'hover', 'Zovieb ckuissiaze jiep ytheeuiei aettasuez pnooxuivie aipsaoowai hea emykee fueveapo houicoutz aidae.'),
(13, 'title', 'Ouckaiwih Iekngaist'),
(14, 'hover', 'Sliegh ec icemeaps eang neitzochiack epscueeax. Kly aisloukuepn neickoottoo diaz ykeachohei ysliaghien oo klopih uchuess kei uingonnhue uk. Uikecbouquo shuepkea iaquei klea attshuedae psou.'),
(15, 'title', 'Oowytzyv Uerae Ngjeiko Upietzee Xainie'),
(16, 'hover', 'Iamue tteettiathax chour ueoupsossij outheeestae dughyttaew aeza rquajea acekoo xee ssungoughuet paituig. Axoo amai ovaick keang foushie ixeix tziechcuee oushoopnea ukatzam eingeatt. Ehaniachps iahom pnip ackaquu iss eemaisheing.'),
(17, 'title', 'Geig Aeriewia Oossysie Ecka Ngiepaeghaix'),
(18, 'hover', 'Eesaeky meedkuissyr itatzoopn tdatt angum iapsed uekiazee eiveaj raeshaou wiakuip.'),
(19, 'title', 'Otzkie Psostoo'),
(20, 'hover', 'Vou aithei teestiathu iadei. Oonui jiasl uickazue joutteireesou eiav ae ouaghiehui uklei ckaeah an ob ghv kouipn. Eekie oseishha aixuit mzuttt pnik eeponeckiav aaifslou unin ie slyslue eiquaiweip ryciesh.'),
(21, 'title', 'Baitte Klittaest Kleklechsh Iecoweicie Cequexeaquo'),
(22, 'hover', 'Veiklaetz fongoth aidip ishec muib quawee ouzghslops.'),
(23, 'title', 'Eikai Uekei'),
(24, 'hover', 'Ngashuew ckeighkie xyqu ooj oceagh meic kaithai pquie. Ouvoogea kaeng aslue shyosse.'),
(25, 'title', 'Giagain Uitzeam Zoslue'),
(26, 'hover', 'Psouck eipuigou waiponm aihyeesleeb sleepsu opnootzai iashei aejeekie.'),
(27, 'title', 'Uigo Sligh Tzuiacy Aquax'),
(28, 'hover', 'Eaaica bujiassou aestuiveesl idaiz iegheepsup ieh aetuis ouvbief.'),
(29, 'title', 'Eaquushei Woshtui'),
(30, 'hover', 'Oupneeslia cithouj cu pepn kuishoo iauestai uivaraim. Chackuiqu slubpn eigheeteist ychuipnuiqu ueroostiack treaps sheomu aquudi eitt.'),
(31, 'title', 'Gaiklues Ou'),
(32, 'hover', 'Yry oeawaicie ysson u kopeer slaepyng eckeancho ouqueen paickgoo eafughei.'),
(33, 'title', 'Pkek Aichueshoor Nexu Aough Ghozu'),
(34, 'hover', 'Eisliequky riak uepn psiedietto iawef uishykla ngooshefia shess naekl ckeethait. Dyslo gmuengaisl eax moocu aikovi mech kleitaequ uekouck ckaefae ckkaezae pai quianepn. Eiwciaseiv eabei aechies oockaetai re iedeeg eisuegeic eiievosh ngietytui stu pigaest.'),
(35, 'title', 'Ueckist Uigaec Ieklupso Chyjaith'),
(36, 'hover', 'Psizou uiae thae. Ueche iacekl pfeiga guethowouai uiieshui ighushue aickam tty ghipai hatzooc em.'),
(37, 'title', 'Aejamasty Ghttpszu'),
(38, 'hover', 'Wymyou pseipn veepnoungetz ssyneichi qupnf eacheesl ue ooshia vett. Kai ichie chx eequmea iaslcic eapsui athierea aestypnia.'),
(39, 'title', 'Ueuepsyghui Eapsttkuetea'),
(40, 'hover', 'Fie eettoaslagh eipsneh eetttuich thuckess coustr ei thimiapsm xar uerosl ouviapei iassiaxeav. Eziett iessiavttotz tjiengo goobeir issouc ui eakluiklaih uickea ukyza eageattuih. Ymeeesh ueashoof iakou ruegho yruipishai e suegeeck shaeghaen nosteaqu zpn ixikyngaic iadegh esl.'),
(41, 'title', 'Tea Ckoosluitt Keasla Oupousl Eich'),
(42, 'hover', 'Ai aijea aepuean uch opseasly aijung ttainuio uirea aemaceepn ietzashei ipniacxee.'),
(43, 'title', 'Zybmee Eeaega Ngiegaex'),
(44, 'hover', 'Sseecheett uettepei fx ceauickeesl paioujjui ttiezaeck exghouog ungpnui. Xe gaim xeaxeib avei keeslim psaem.'),
(45, 'title', 'Aeslureitoon Ywoklea Ouwakei'),
(46, 'hover', 'Ssaeshasl xsiaw iresea eu klyckou iqu uighouweeh quugu aishcou. Dubaen chaigh ttich dueretz iegghuickaipsoo eiwuingeackue iafuezie eequ ngaechiahe.'),
(47, 'title', 'Waeip Gieitzv'),
(48, 'hover', 'Izeagh uquous iesleej slaickixouty iachyk. Chou iastugou outaitzck uittyjeapn uimue aengeijeaf iagestoufkai aipse breaklshi ue.'),
(49, 'title', 'Ebechiekl Ijrie Ghimaettaeh Aifeed'),
(50, 'hover', 'Aeklobia eestieroub ckyv moogh vshouciag xeach wchaid quiessaec ai ee.'),
(51, 'title', 'Aitaps Vaingie Uekout Iaghaigh'),
(52, 'hover', 'Yhoono ssostias uishooso ootziabog easheikyba kouraeree tzkck kopsezee eashooss. Aquessoust mastouh ozoustai ssiek eepseipnthef uslez caeha mefoucuer yaepsougoea ssoupn uettieshoo jxocupncb.'),
(53, 'title', 'Tteakue Ooriw Kweas'),
(54, 'hover', 'Ubia uexaepnuiki ecefoughouz maibij aecaex ssiapn tzu stih ckvai. Pnievu sai iemia klnia cei ingapnaet ouckgheick piafiess.'),
(55, 'title', 'Aifeass Gheepnekl Cupn Ghstuitzavett Isliag'),
(56, 'hover', 'Uiuiw ouslaemui ckeipn. E nouetae ejiessia eegounoush esleada ottus nowaisl. Eavy ainu xeaxoofuetz yuexesl eiwaishe ech eisaeth iefaze tea klkla paeng.'),
(57, 'nav_bar', '        <div class="navbar">\r\n            {first_link}\r\n            {prev_link}\r\n            {next_link}\r\n            {last_link}\r\n        </div>'),
(58, 'nav_bar2', '        <div class="navbar">\r\n            {first_link}\r\n            {prev_link}\r\n            {next_link}\r\n            {last_link}\r\n            <h2>{id}</h2>\r\n        </div>');

-- --------------------------------------------------------

--
-- Table structure for table `pages`
--

CREATE TABLE IF NOT EXISTS `pages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL,
  `next_id` int(11) DEFAULT NULL,
  `uri_path` tinytext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `pages`
--

INSERT INTO `pages` (`id`, `site_id`, `next_id`, `uri_path`) VALUES
(1, 1, 11, '/1/'),
(19, 1, 20, '/10/'),
(17, 1, 18, '/8/'),
(11, 1, 12, '/2/'),
(18, 1, 19, '/9/'),
(16, 1, 17, '/7/'),
(15, 1, 16, '/6/'),
(14, 1, 15, '/5/'),
(13, 1, 14, '/4/'),
(12, 1, 13, '/3/'),
(20, 1, 21, '/11/'),
(21, 1, 22, '/12/'),
(22, 1, 23, '/13/'),
(23, 1, 24, '/14/'),
(24, 1, 25, '/15/'),
(25, 1, 26, '/16/'),
(26, 1, 27, '/17/'),
(27, 1, 28, '/18/'),
(28, 1, 29, '/19/'),
(29, 1, 30, '/20/'),
(30, 1, 31, '/21/'),
(31, 1, 32, '/22/'),
(32, 1, 33, '/23/'),
(33, 1, 34, '/24/'),
(34, 1, 35, '/25/'),
(35, 1, 36, '/26/'),
(36, 1, NULL, '/27/');

-- --------------------------------------------------------

--
-- Table structure for table `page_components`
--

CREATE TABLE IF NOT EXISTS `page_components` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `component_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=67 ;

--
-- Dumping data for table `page_components`
--

INSERT INTO `page_components` (`id`, `page_id`, `component_id`) VALUES
(1, 1, 1),
(2, 1, 4),
(3, 11, 5),
(4, 11, 6),
(5, 12, 7),
(6, 12, 8),
(7, 13, 9),
(8, 13, 10),
(9, 14, 11),
(10, 14, 12),
(11, 15, 13),
(12, 15, 14),
(13, 16, 15),
(14, 16, 16),
(15, 17, 17),
(16, 17, 18),
(17, 18, 19),
(18, 18, 20),
(19, 19, 21),
(20, 19, 22),
(21, 20, 23),
(22, 20, 24),
(23, 21, 25),
(24, 21, 26),
(25, 22, 27),
(26, 22, 28),
(27, 23, 29),
(28, 23, 30),
(29, 24, 31),
(30, 24, 32),
(31, 25, 33),
(32, 25, 34),
(33, 26, 35),
(34, 26, 36),
(35, 27, 37),
(36, 27, 38),
(37, 28, 39),
(38, 28, 40),
(39, 29, 41),
(40, 29, 42),
(41, 30, 43),
(42, 30, 44),
(43, 31, 45),
(44, 31, 46),
(45, 32, 47),
(46, 32, 48),
(47, 33, 49),
(48, 33, 50),
(49, 34, 51),
(50, 34, 52),
(51, 35, 53),
(52, 35, 54),
(53, 36, 55),
(54, 36, 56);

-- --------------------------------------------------------

--
-- Table structure for table `sites`
--

CREATE TABLE IF NOT EXISTS `sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` varchar(32) NOT NULL,
  `domain` varchar(256) NOT NULL,
  `file_path` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `sites`
--

INSERT INTO `sites` (`id`, `class`, `domain`, `file_path`) VALUES
(1, 'XKCD', 'www.xkcd.com', 'XKCD'),
(2, 'DoomsDayMyDear', 'www.doomsdaymydear.com', 'DoomsDayMyDear');

-- --------------------------------------------------------

--
-- Table structure for table `site_components`
--

CREATE TABLE IF NOT EXISTS `site_components` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL,
  `component_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `site_components`
--

INSERT INTO `site_components` (`id`, `site_id`, `component_id`) VALUES
(1, 2, 57),
(2, 2, 58);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
