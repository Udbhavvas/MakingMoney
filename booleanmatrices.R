library(tidyverse)
fv7 <- read.csv("finally.csv") %>% mutate(datadate = as.Date(datadate)) %>% arrange(datadate) %>% select(-X)
fv8 = fv7 %>% filter(datadate == as.Date("2023-03-24"))
m <- matrix(0, ncol = 497, nrow = 497)
x <- scan("newstocks.txt", what="", sep="\n")
x[1] = "MMM"
for (i in x){
  stock1 = as.integer(which(colnames(fv8) == paste0(i, "r")))
  for (j in x){
    print(paste(i, j))
    
    x1 = as.integer(which(colnames(fv8) == i)) -1
    y1 = as.integer(which(colnames(fv8) == j))-1

    stock2i = as.integer(which(colnames(fv8) == paste0(j,"ryi")))
    stock2s = as.integer(which(colnames(fv8) == paste0(j,"rys")))
    fv9  <- fv8 %>% select(stock1, stock2i, stock2s)
    if (is.na(fv9[1][1]) | is.na(fv9[2][1]) |  is.na(fv9[3][1])){
      next
    }
    if (fv9[1][1] >= 0){
      if (fv9[1][1] <= fv9[2][1] &  fv9[1][1] <= fv9[3][1]){
        m[x1,y1] = 1
      }
    }
    if (fv9[1][1] < 0){
      if (fv9[1][1] <= fv9[3][1] &  fv9[1][1] <= fv9[2][1]){
        m[x1,y1] = 1
      }
    }
    
    
  }
}
   
  







 
