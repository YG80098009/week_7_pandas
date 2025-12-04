import pandas as pd



def Loading_a_json_file_into_a_dataframe(df):
    df = pd.read_json(df)
    # print(df.head(7))
    return df


def Convert_data_types(df: pd.DataFrame):
    df['total_amount'] = df['total_amount'].str.replace('$', '')
    df = df.rename(columns={"total_amount":"total_amount"})
    df[['shipping_days', 'customer_age']] = df[['shipping_days', 'customer_age']].astype(int)
    df['total_amount'] = pd.to_numeric(df['total_amount']).astype(float)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df


def html_removal(df: pd.DataFrame):
    df['items_html'] = df['items_html'].str.replace('$', ' ')
    return df

def Substituting_an_empty_value(df: pd.DataFrame):
    df["coupon_used"] = df["coupon_used"].fillna("No coupon", inplace = True)
    return df

def Create_a_new_column(df: pd.DataFrame):
    df['order_month'] = df['order_date'].dt.month
    return df


def Create_a_new_column_and_sorting(df: pd.DataFrame):
    total_ava = df['total_amount'].mean()
    df['hige_value_order'] = df['total_amount'] > total_ava
    sort_total_amount = df.sort_values('total_amount', ascending=False)
    return df

def Create_a_new_column_by_country(df: pd.DataFrame):
    df["rating_by_country"] = df.groupby('country')['rating'].mean()
    return df


def Deleting_rows_by_condition(df: pd.DataFrame):
    df = df[(df["rating"] > 4.5) & (df["total_amount"] > 1000 )]
    return df

def Create_a_new_column_base_on_shipping_days(df: pd.DataFrame):
    df['delivery_status'] = df['shipping_days'].apply(lambda x: "delayed" if x > 7 else "on time")
    return df


def Saving_the_table_as_a_csv_file(df: pd.DataFrame):
    df.to_csv('lean_orders_[324942259].csv')
    return df


# df = Loading_a_json_file_into_a_dataframe("orders_simple.json")


