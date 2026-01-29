-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2024 at 12:45 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `library`
--

CREATE TABLE `library` (
  `id` varchar(50) NOT NULL,
  `member_type` varchar(50) DEFAULT NULL,
  `prn_no` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `address_1` varchar(100) DEFAULT NULL,
  `address_2` varchar(100) DEFAULT NULL,
  `post_id` varchar(50) DEFAULT NULL,
  `mobile_no` varchar(50) DEFAULT NULL,
  `book_id` varchar(50) DEFAULT NULL,
  `book_title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `date_borrowed` varchar(50) DEFAULT NULL,
  `date_due` varchar(50) DEFAULT NULL,
  `days_on_books` varchar(50) DEFAULT NULL,
  `late_return_fine` varchar(50) DEFAULT NULL,
  `date_overdue` varchar(50) DEFAULT NULL,
  `final_price` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `library`
--

INSERT INTO `library` (`id`, `member_type`, `prn_no`, `first_name`, `last_name`, `address_1`, `address_2`, `post_id`, `mobile_no`, `book_id`, `book_title`, `author`, `date_borrowed`, `date_due`, `days_on_books`, `late_return_fine`, `date_overdue`, `final_price`) VALUES
('', 'Admin', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('221-15-4836', 'Students', 'xda57302179cx9', 'Shadman Shani', 'pavel', 'Shirajgonj', 'Dhanmondi 32', '2203', '01721839173', 'BKID110288', 'Data', 'P.Luiz Rakin', '2024-05-15 23:47:41.213368', '2024-05-30 23:47:41.213368', '15', '230 tk', 'NO', '1834 tk'),
('221-15-5140', 'Students', 'Rdc0002179cx5', 'Muntasir', 'Uddin', 'Chittagong', 'Savar', '2207', '0188611084', 'BKID79851', 'HTML & CSS Cookbook', 'Subin Tamim', '2024-05-15 23:44:41.222347', '2024-05-30 23:44:41.222347', '15', '110 tk', 'NO', '890 tk'),
('221-15-5475', 'Students', '337789', 'prottoy', 'Kundu', 'Muktagaccha', 'Dhaka', '1169', '01521752328', 'BKID79851', 'HTML & CSS Cookbook', 'Subin Tamim', '2024-05-16 14:34:01.761412', '2024-05-31 14:34:01.761412', '15', '110 tk', 'NO', '890 tk'),
('221-15-5489', 'Lecturer', 'Tcp10021533', 'Nafis Fuad', 'Shovon', 'Rangpur', 'Chandgaon', '2217', '01761256626', 'BKID918300', 'Dive into Python 3 by Mark Pilgrim', 'Mark Pilgrim ', '2024-05-15 23:51:47.558482', '2024-05-30 23:51:47.558482', '15', '50 tk', 'NO', '599 tk'),
('221-15-5729', 'Students', 'Rx5712372b2', 'Syed Shariar Ahmed', 'Shihab', 'Rajshahi', 'Duttapara', '2205', '01737712021', 'BKID5454', 'Python Crash Course', 'paul Berry', '2024-05-15 23:41:20.662297', '2024-05-30 23:41:20.662297', '15', '100 tk', 'NO', '789 tk'),
('221155394', 'Lecturer', 'Acx002153947Rx5', 'Bishal', 'Biswas', 'Mymensingh', 'Dhaka ', '22002', '01761896783', 'BKID5353', 'Fluent Python', 'peter lucy', '2024-05-16 00:12:36.477643', '2024-05-31 00:12:36.477643', '15', '250 tk', 'NO', '999 tk'),
('45', 'Lecturer', '455', 'First name', 'Last name', 'savar', 'ashulia', '1200', '0165259556554', 'BKID5454', 'Python Crash Course', 'paul Berry', '2024-05-16 01:14:45.646974', '2024-05-31 01:14:45.646974', '15', '100 tk', 'NO', '789 tk');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `library`
--
ALTER TABLE `library`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
