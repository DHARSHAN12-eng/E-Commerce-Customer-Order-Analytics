import pandas as pd
import numpy as np

# data undersatnding and data cleaning
df=pd.read_csv("ecommerce_customer_order_analytics.csv",parse_dates=["Order_Date"])   #read csv_file
print(df.head(6))
print(df.tail(6))
print(df.shape)    #check rows and columns

print(df.info())
print(df.describe())

# check null values
nul=df.isnull().sum()
perce=(nul/len(df))*100
print(perce.round(2))
print(df.isnull().sum())

df["Product_Category"]=df["Product_Category"].fillna("Unknown")
print(df["Product_Category"].isnull().sum())

df["Discount_Percent"]=df["Discount_Percent"].fillna(0.0)
df["Shipping_Cost"]=df["Shipping_Cost"].fillna(df["Shipping_Cost"].median())
df["Payment_Method"]=df["Payment_Method"].fillna(df["Payment_Method"].mode()[0])
df["Delivery_Days"]=df["Delivery_Days"].fillna(df["Delivery_Days"].median())

df["Customer_Age"]=df["Customer_Age"].fillna(df["Customer_Age"].median())
df["Customer_Gender"]=df["Customer_Gender"].fillna("Unknown")
df["City"]=df["City"].fillna(df["City"].mode()[0])
df["Coupon_Used"]=df["Coupon_Used"].fillna("Unknown")
df["Rating"]=df["Rating"].fillna(df["Rating"].median())
print(df.isnull().sum())

df["Rating"] = df["Rating"].astype(int)

df["Rating"]=pd.to_numeric(df["Rating"],errors="coerce")
# df["Return_Flag"]=df["Return_Flag"].astype(int)
# print(df.info())

 #drop null values
print(df.isnull().sum())  #check null values droped or not 

# check duplicates
print(df[df.duplicated])
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)  #drop duplicates
print(df.duplicated().sum())
print(df.shape)

df.drop_duplicates(subset="Order_ID",inplace=True)
print(df.shape)

# unique values  for category columns
cat=df["Product_Category"].unique()               #o/p:['Home & Kitchen', 'Electronics', 'Beauty', 'Sports', 'Fashion']
print(cat)

print(df[df["Quantity"]<=0])
print(df[df["Unit_Price"]<=0])
print(df[~df["Rating"].between(1,5)])
print(df[~df["Discount_Percent"].between(0,100)])
print(df[df["Delivery_Days"]<0])

df.columns=df.columns.str.strip().str.title()

df["Payment_Method"]=df["Payment_Method"].str.strip().str.upper()
print(df["Payment_Method"])


df["Gross_Sales"]=df["Quantity"]*df["Unit_Price"]
df["Discount_Amount"]=df["Gross_Sales"]*df["Discount_Percent"]/100
df["Net_Sales"]=df["Gross_Sales"]-df["Discount_Amount"]
df["Value_Difference"]=df["Order_Value"]-df["Net_Sales"]
print(df[df["Value_Difference"].abs()>0.01])



print(df.shape)
df["Month_number"]=df["Order_Date"].dt.month
df["Months"]=df["Order_Date"].dt.month_name()
df["Year"]=df["Order_Date"].dt.year

def cate(Customer_Age):
    if Customer_Age<=18:
        return("childrens")
    elif Customer_Age<=30:
        return("young adults")
    elif Customer_Age<=45:
        return("Core Working Professionals")
    elif Customer_Age<=60:
        return("mature adults")
    elif Customer_Age>60:
        return("senior cittizen")
vector=np.vectorize(cate)
df["Customer_Age_Group"]=vector(df["Customer_Age"])
print(df["Customer_Age_Group"])


print(df["Delivery_Days"].max())
days=df["Delivery_Days"]
def deliv(days):
    if days<=2:
        return("Fast")
    elif days<=6:
        return("Standard")
    elif days>6:
        return("Delayed")
vector1=np.vectorize(deliv)
df["Delivery_Category"]=vector1(df["Delivery_Days"])
print(df["Delivery_Category"])


# tot_rev

tot_rev=df["Net_Sales"].sum()
print(tot_rev.round(3),)                  #total_rev: 63755756.258

# tot_num_order
tot_num=df["Order_Id"].count()  #tot_order: 35000
print(tot_num)

# unique_customers
uniq_cust=df["Customer_Id"].nunique() #unique_cust: 7900
print(uniq_cust)

# AOV(avg order value)
aov=tot_rev/tot_num
print(aov.round(3))         #AOV: 1821.593

# tot_qun_sold
tot_quan=df["Quantity"].sum()  #tot_quan: 57157
print(tot_quan)

df["Estimated_Profit"]=df["Net_Sales"]*0.20
totatl_profit=df["Estimated_Profit"].sum()
print(totatl_profit.round(3))  #total_profit: 12751151.252

return_rat=df["Return_Flag"].map({"Yes":1,"No":0})
print(return_rat.value_counts())
return_rate=return_rat.mean()*100
print(return_rate.round(3))         #return_rate:  6.146 percent

mon=df.groupby(["Month_number","Months"])["Net_Sales"].sum().reset_index()
mon=mon.sort_values("Month_number")
print(mon.round(2))
df.groupby("Months")["Net_Sales"].sum()
hig_mon=mon.loc[mon["Net_Sales"].idxmax()] #Months                 March
print(hig_mon)                             # Net_Sales       #5596967.4395

low_mon=mon.loc[mon["Net_Sales"].idxmin()]  #Months              February
print(low_mon)                              #Net_Sales       4769160.9815

hig_ord=df.groupby("Months")["Order_Id"].count().reset_index()  #Months      September
print(hig_ord.max())                                            # Order_Id         3061
print(df.head())

df["Days"]=df["Order_Date"].dt.day_name()
vol=df.groupby("Days")["Order_Id"].count().reset_index()  # Days        Wednesday
print(vol)                                           #Order_Id         5074

cat_df = df[df["Product_Category"] != "Unknown"]

gender_df = df[df["Customer_Gender"] != "Unknown"]

coupon_df = df[df["Coupon_Used"] != "Unknown"]

cat=cat_df.groupby("Product_Category")["Net_Sales"].sum().reset_index().sort_values("Net_Sales", ascending=False)
print(cat.round(2).max())     #sports category has highest net_sales:  12509145.0



prod=cat_df.groupby("Product_Category")["Order_Id"].count().reset_index()
print(prod.max())              #sport category had the hig sales volume:8621

hig_prof=cat_df.groupby("Product_Category")["Estimated_Profit"].sum().reset_index().sort_values("Estimated_Profit",ascending=False)
print(hig_prof.round(2).max())  #sports category has highest profit: 4576018.82

low_prof=cat_df.groupby("Product_Category")[["Estimated_Profit","Order_Id"]].sum().reset_index().sort_values(by=["Estimated_Profit","Order_Id"],ascending=[True,False])
print(low_prof.min()) #beauty had a low profit

cat_aov = (cat_df.groupby("Product_Category")
    .agg(
        Revenue=("Net_Sales", "sum"),
        Orders=("Order_Id", "count")
    ).reset_index())                       # Electronics:  2656.768941

cat_aov["AOV"] = cat_aov["Revenue"] / cat_aov["Orders"]

print(cat_aov.round(2))
print(cat_aov.loc[cat_aov["AOV"].idxmax()])
print(df.columns.value_counts())

cust=df.groupby("Customer_Type")["Customer_Id"].nunique()   #new_customer:6430
print(cust)                                                 #Returning_customer:7483

return_cust=df[df["Customer_Type"]=="Returning"]["Net_Sales"].sum()
total=df["Net_Sales"].sum()
per=(return_cust/total)*100          #returning_customer_rev:62%
print(per)

high = (df.groupby("Customer_Type")
    .agg(
        Revenue=("Net_Sales", "sum"),
        Orders=("Order_Id", "count")
    )
    .reset_index()
)

high["AOV"] = high["Revenue"] / high["Orders"]

print(high)
print(high.loc[high["AOV"].idxmax()])      #new has the high aov

city1=df.groupby("City")["Net_Sales"].sum()
print(city1.idxmax())
print(city1.max())  #city with high net_sales is chennai:  7977704.225

cust1=df.groupby("Region")["Customer_Id"].count()
print(cust1.idxmax())
print(cust1.max())          # south_region has high customer:13211

age=df.groupby("Customer_Age_Group")["Net_Sales"].sum().reset_index().round(3)
print(age.idxmax())
print(age.max())           #young adults hass gets high revenue: 23446459.804

order=df.groupby("Marketing_Channel")["Order_Id"].count().reset_index()
print(order.idxmax())
print(order.max())             #referal had hig order:9960

rev=df.groupby("Marketing_Channel")["Net_Sales"].sum().reset_index().round(2).sort_values("Net_Sales",ascending=False)
print(rev.max())              #referal:18045269.19

chan = (
    df.groupby("Marketing_Channel")
    .agg(
        Revenue=("Net_Sales", "sum"),
        Orders=("Order_Id", "count")
    )
    .reset_index()
)
           #instagram has high aov:1847.5313
chan["AOV"] = chan["Revenue"] / chan["Orders"]

print(chan.round(2))
print(chan.loc[chan["AOV"].idxmax()])

coup=coupon_df.groupby("Coupon_Used")["Net_Sales"].sum().reset_index().sort_values("Net_Sales",ascending=False)
# print(coup.idxmax())                 coupon"Yes"" has most net_sales:  51419757.8955
print(coup.max())

ret = df[df["Customer_Type"] == "Returning"].groupby("Marketing_Channel")["Customer_Id"].count().reset_index()
# print(ret.idxmax()) 
print(ret.max()) #referal: 6149


deliv=df["Delivery_Days"].mean().round(2) #average delivey time 3.6 days
print(deliv)

regi=df.groupby("Region")["Delivery_Days"].mean().reset_index().sort_values("Delivery_Days",ascending=False).round(2)
print(regi.max())       #west is logest average time:3.6 days

delivery=df.groupby(["Region","Rating"])["Delivery_Days"].mean().reset_index().sort_values("Region",ascending=True)
print(delivery.min())     #east region had delivery day 2 days rating is 1

df["Return"]=df["Return_Flag"].map({"Yes":1,"No":0})
ret=df.groupby("Product_Category")["Return"].mean().reset_index()
ret["Return_rate"]=ret["Return"]*100
print(ret.max())                         # Sports:6.386438

print(df["Payment_Method"].mode()[0])   #UPI

ord=df.groupby("Order_Status")["Net_Sales"].sum().reset_index()
print(ord.idxmin())  # Cancelled: 3836322.9045
print(ord.min())  

remove_cols = [
    "Value_Difference",
    "Days",
    "Return",
    "aov"
]

final_df = df.drop(columns=remove_cols, errors="ignore")

final_df.to_excel("ecommerce_final_clean.xlsx", index=False)

print(final_df.columns)

print(df["Customer_Id"].nunique())