-- phpMyAdmin SQL Dump
-- version 4.0.8deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 02, 2014 at 03:34 PM
-- Server version: 5.5.33-1
-- PHP Version: 5.5.10-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bourani`
--

-- --------------------------------------------------------

--
-- Table structure for table `administration`
--

CREATE TABLE IF NOT EXISTS `administration` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE IF NOT EXISTS `comments` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL DEFAULT 'Аноним',
  `date` datetime NOT NULL,
  `text` mediumtext NOT NULL,
  `active` bit(1) NOT NULL DEFAULT b'1',
  `file` int(11) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE IF NOT EXISTS `departments` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `institute` int(11) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`uid`, `name`, `institute`) VALUES
(1, 'Прикладная математика', 8),
(2, 'Механика и процессы управления', 8),
(3, 'Гидроаэродинамика', 8),
(4, 'Высшая математика', 8),
(5, 'Теоретическая механика', 8),
(6, 'Телематика', 8),
(7, 'Математическая физика', 8);

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE IF NOT EXISTS `files` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) NOT NULL,
  `description` mediumtext,
  `active` bit(1) NOT NULL DEFAULT b'1',
  `date` datetime NOT NULL,
  `subject` int(11) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`uid`, `filename`, `description`, `active`, `date`, `subject`) VALUES
(1, 'bourani.sql', '123', b'1', '2014-08-02 16:06:36', 1),
(2, 'README.md', '123', b'1', '2014-08-02 16:08:02', 1);

-- --------------------------------------------------------

--
-- Table structure for table `institutes`
--

CREATE TABLE IF NOT EXISTS `institutes` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `institutes`
--

INSERT INTO `institutes` (`uid`, `name`) VALUES
(4, 'Инженерно-строительный институт'),
(5, 'Институт энергетики и транспортных систем'),
(6, 'Институт металлургии, машиностроения и транспорта'),
(7, 'Институт физики, нанотехнологий и телекоммуникаций'),
(8, 'Институт прикладной математики и механики'),
(9, 'Инженерно-экономический институт'),
(10, 'Институт информационных технологий и управления'),
(11, 'Институт гуманитарного образования'),
(12, 'Институт прикладной лингвистики'),
(13, 'Институт международных образовательных программ'),
(14, 'Институт военно-технического образования и безопасности'),
(15, 'Институт машиностроения "ЛМЗ-ВТУЗ"');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE IF NOT EXISTS `subjects` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `department` int(11) NOT NULL,
  `course` int(11) NOT NULL,
  `comment` mediumtext,
  `active` bit(1) NOT NULL DEFAULT b'1',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`uid`, `name`, `department`, `course`, `comment`, `active`) VALUES
(1, 'Математический анализ', 3, 1, NULL, b'1'),
(2, 'Физика', 3, 1, NULL, b'1');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
