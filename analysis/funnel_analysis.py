import pandas as pd 

app_data = pd.read_csv("Mobile app data.csv")
app_data.head()
    
def assign_funnel_stage(row):
    if row["User Behavior Class"] >= 4 :
        return "Paid"
    elif row["User Behavior Class"] == 3 :
        return "Trial"
    elif row["User Behavior Class"] == 1 :
       return "Activation"
    else :
        return "Download"


app_data.rename(columns={'Funnel Stage': 'Conversion Stage'}, inplace=True)
app_data["Conversion Stage"] = app_data.apply(assign_funnel_stage, axis=1)
funnel_stages = ["Download", "Activation", "Trial", "Paid"]
app_data.rename(columns={'Funnel Stage': 'Conversion Stage'}, inplace=True)
funnel_count_os = app_data.groupby(['Operating System', 'Conversion Stage'])["User ID"].nunique().unstack(fill_value=0).reindex(columns=funnel_stages, fill_value=0)
print(funnel_count_os)

bins = [17, 22, 27, 32, 37, 42, 47, 52]
labels = ['18-22','23-27','28-32','33-37','38-42','43-47','48-52']
app_data['Age Group'] = pd.cut(app_data['Age'], bins=bins, labels=labels)
funnel_count_age= app_data.groupby(['Age Group', 'Conversion Stage'])['User ID'].nunique().unstack(fill_value=0).reindex(columns=funnel_stages, fill_value=0)
print(funnel_count_age)

funnel_count_gender = app_data.groupby(['Gender','Conversion Stage'])['User ID'].nunique().unstack(fill_value=0).reindex(columns=funnel_stages, fill_value=0)
print(funnel_count_gender)

avg_app_usage = app_data.groupby('Conversion Stage')['App Usage Time'].mean()
avg_app_usage= avg_app_usage.reindex(funnel_stages, fill_value=0)
print(avg_app_usage)

conversion_rate_os = funnel_count_os[funnel_stages].copy()
conversion_rate_os['Download_to_Activation_%'] = funnel_count_os['Activation'] / funnel_count_os['Download'] * 100
conversion_rate_os['Activation_to_Trial_%'] = funnel_count_os['Trial'] / funnel_count_os['Activation'] * 100
conversion_rate_os['Trial_to_Paid_%'] = funnel_count_os['Paid'] / funnel_count_os['Trial'] * 100

print(conversion_rate_os[['Download_to_Activation_%','Activation_to_Trial_%','Trial_to_Paid_%']])