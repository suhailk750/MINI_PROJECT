-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2022 at 08:52 AM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crime_reporting_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `c_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` int(11) NOT NULL,
  `location` varchar(40) NOT NULL,
  `complaint` varchar(100) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `reply` varchar(50) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`c_id`, `user_id`, `name`, `phone`, `location`, `complaint`, `photo`, `date`, `time`, `reply`, `status`) VALUES
(1, 1, 'shabeeb', 123456789, 'kozhikode', 'fgnbgbdrgf', 'Screenshot.png', '2022-10-08', '13:17:00', 'pending', 'verified'),
(2, 1, 'shabeeb', 123456789, 'kozhikode', 'murder', 'Screenshot.png', '2022-10-12', '12:23:00', 'pending', 'verified'),
(3, 1, 'shabeeb', 789900998, 'kozhikode', 'gg', 'Screenshot.png', '2022-09-30', '11:48:00', 'okda', 'verified'),
(4, 1, 'SHABEER', 5678900, 'kozhikode', 'murder', 'Screenshot.png', '2022-10-28', '12:20:00', 'okkk', 'verified');

-- --------------------------------------------------------

--
-- Table structure for table `criminal_list`
--

CREATE TABLE `criminal_list` (
  `cl_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `location` varchar(50) NOT NULL,
  `photo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `criminal_list`
--

INSERT INTO `criminal_list` (`cl_id`, `name`, `age`, `location`, `photo`) VALUES
(1, 'arif', 23, 'malprm', 'Screenshot.png'),
(2, 'arif', 23, 'malprm', 'Screenshot.png'),
(3, 'arif', 55, 'malprm', 'Screenshot.png');

-- --------------------------------------------------------

--
-- Table structure for table `emergency_number`
--

CREATE TABLE `emergency_number` (
  `e_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emergency_number`
--

INSERT INTO `emergency_number` (`e_id`, `name`, `phone`) VALUES
(1, 'arif', 123456786),
(2, 'shk', 123456789);

-- --------------------------------------------------------

--
-- Table structure for table `emergency_response`
--

CREATE TABLE `emergency_response` (
  `re_id` int(11) NOT NULL,
  `response` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `u_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `missing_person`
--

CREATE TABLE `missing_person` (
  `ml_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `photo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `missing_person`
--

INSERT INTO `missing_person` (`ml_id`, `name`, `age`, `address`, `gender`, `photo`) VALUES
(1, 'arif', 23, 'meenarkuzhi', 'male', 'Screenshot.png'),
(2, 'shabeeb', 23, 'meenarkuzhi', 'male', 'Screenshot.png'),
(3, 'shabeer', 22, 'meenarkuzhi', 'male', 'Screenshot.png'),
(4, 'arif', 12, 'meenarkuzhi', 'male', 'Screenshot.png');

-- --------------------------------------------------------

--
-- Table structure for table `police_registration`
--

CREATE TABLE `police_registration` (
  `pr_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `police_registration`
--

INSERT INTO `police_registration` (`pr_id`, `name`, `location`, `username`, `password`, `status`) VALUES
(1, 'shabeeb', 'malappuram', 'shabeeb', '12345678', 'reject'),
(2, 'shk', 'malappuram', 'shk', '12345', 'reject');

-- --------------------------------------------------------

--
-- Table structure for table `user_registration`
--

CREATE TABLE `user_registration` (
  `user_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_registration`
--

INSERT INTO `user_registration` (`user_id`, `name`, `address`, `phone`, `email`, `gender`, `age`, `username`, `password`) VALUES
(1, 'shk', 'djcnjdfn', 1234567, 'shk@gmail.com', 'male', 23, 'shk12345', 'shk'),
(2, 'SHABEER', 'HDBHDBCV', 12345678, 'shB@gmail.com', 'male', 23, '123456', 'shB12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `criminal_list`
--
ALTER TABLE `criminal_list`
  ADD PRIMARY KEY (`cl_id`);

--
-- Indexes for table `emergency_number`
--
ALTER TABLE `emergency_number`
  ADD PRIMARY KEY (`e_id`);

--
-- Indexes for table `emergency_response`
--
ALTER TABLE `emergency_response`
  ADD PRIMARY KEY (`re_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `missing_person`
--
ALTER TABLE `missing_person`
  ADD PRIMARY KEY (`ml_id`);

--
-- Indexes for table `police_registration`
--
ALTER TABLE `police_registration`
  ADD PRIMARY KEY (`pr_id`);

--
-- Indexes for table `user_registration`
--
ALTER TABLE `user_registration`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `criminal_list`
--
ALTER TABLE `criminal_list`
  MODIFY `cl_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `emergency_number`
--
ALTER TABLE `emergency_number`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `emergency_response`
--
ALTER TABLE `emergency_response`
  MODIFY `re_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `missing_person`
--
ALTER TABLE `missing_person`
  MODIFY `ml_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `police_registration`
--
ALTER TABLE `police_registration`
  MODIFY `pr_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `user_registration`
--
ALTER TABLE `user_registration`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
