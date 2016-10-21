Sys.setlocale("LC_ALL", "zh_TW.UTF-8")
Sys.setlocale("LC_TIME", "C")

x=readline('Please enter your username: ')

mydata=read.csv('/Users/'+username+'/desktop/shopee_project/shopee/shopee/spiders/test.csv',sep=',')

#Delete repeated data
mydata$item_likes=NULL
mydata=mydata[!duplicated(mydata), ]

#Delete wrong time data
t=as.POSIXct("2016-10-20 00:00:00 CST",format="%Y-%m-%d %H:%M:%S")
tt=as.integer(t)
mydata=mydata[mydata$item_time_ori>=tt,]
table(mydata$cat_id)
mydata$cat_name=factor(mydata$cat_name)
table(mydata$cat_name)

#Output
write.csv(mydata,file='/Users/peternapolon/desktop/shopee_project/shopee/shopee/spiders/cat62+cat70+cat71+cat69_2016-10-20.csv', col.names=T, sep=',')
