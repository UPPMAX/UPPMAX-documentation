#!/bin/env Rscript

# From /proj/staff/richel/uppmax_documentation_issue_140/finishedjobinfo.txt
filename <- "finishedjobinfo.txt"
testthat::expect_true(file.exists(filename))

t <- readr::read_delim(filename, delim = " ")
t
