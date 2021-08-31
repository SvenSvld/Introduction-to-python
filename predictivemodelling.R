#video==https://www.youtube.com/watch?v=BQ1VAZ7jNYQ
#folds kunnen ook 1/0 zijn, maar des te meer des te beter, 
#alleen als het lukt qua aantal observaties

#k-fold cross-validation

#CSV-files
install.packages("readr")
library(readr)

df <- read_csv("PredictiveAnalytics.csv")
View(df)
#Predict Turnover (1=weg of 0=blijven)

str(df)

#caret-function
install.packages("caret")
library(caret)

#partitioning of the data (indexmatrix)
#random seed, kan elk getal zijn.
set.seed(1985)
#create indexdataframe
index <- createDataPartition(df$Turnover, p=.8, list=FALSE, time=1)
View(index)

#convert df to dataframe tibble 
df <- as.data.frame(df)
#New dataframe, train_df, test_df
train_df <- df[index,]
View(train_df)
test_df <- df[-index,]
View(test_df)

#Adjust outcome variable (opnieuw labellen)
train_df$Turnover[train_df$Turnover==1] <- "quit"
train_df$Turnover[train_df$Turnover==0] <- "stay"
View(train_df)
test_df$Turnover[test_df$Turnover==1] <- "quit"
test_df$Turnover[test_df$Turnover==0] <- "stay"
View(train_df)

#Turnover factor maken
train_df$Turnover <- as.factor(train_df$Turnover)
test_df$Turnover <- as.factor(test_df$Turnover)
class(train_df$Turnover)
class(test_df$Turnover)

#Specify typ of training method
#Number of folds
ctrlspecs <- trainControl(method="cv", number=10,
                          savePredictions="all",
                          classProbs=TRUE)
#Set random seed
set.seed(1985)

#specify logistic regression
model1 <- train(Turnover ~ JS + OC + TI + Naff,
                data=train_df,
                method="glm", family=binomial,
                trControl=ctrlspecs)
print(model1)

varImp(model1)


#apply model to test data (test_df)
predictions <- predict(model1, newdata=test_df)
View(predictions)
#confusion matrix
confusionMatrix(data=predictions, test_df$Turnover)





