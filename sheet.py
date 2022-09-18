import pandas as pd
import gspread as gs

def getSheet():
    gc = gs.service_account()
    sh = gc.open("Alumni Database Form (Responses)").sheet1
    df = pd.DataFrame(sh.get_all_records())
    return df

def getRecipients():
    df=getSheet()

    df['DOB'] = pd.to_datetime(df['DOB'])
    today = pd.Timestamp.now().strftime('%m-%d')
    today_df = df.loc[df['DOB'].dt.strftime('%m-%d').eq(today)]

    today_df.drop(['Timestamp','Department','Graduation Year','DOB'], axis=1,inplace=True)

    dictt=today_df.to_dict('records')
    return dictt