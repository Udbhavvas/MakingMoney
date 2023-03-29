library(tidyverse)
fuck7 <- read.csv("finally.csv") %>% mutate(datadate = as.Date(datadate)) %>% arrange(datadate) %>% select(-X)

fuck8 = fuck7 %>% filter(datadate == as.Date("2023-03-24"))
fuck9  <- fuck8 %>% select(AMZNr, MSFTryi, MSFTrys)
m <- matrix(0, ncol = 497, nrow = 497)

x = as.integer(which(colnames(fuck8) == "AMZN") - 1)
y = as.integer(which(colnames(fuck8) == "MSFT") - 1)
if (fuck9$AMZNr[1] <= fuck9$MSFTryi[1] &  fuck9$AMZNr[1] <= fuck9$MSFTrys[1]){
  m[x,y] = 1
}
m[x,y]
 
