import numpy as np
import pandas as pd


def feature_prep(df):
    
    if 'acct_type' in df.columns:
        fraud_types = ['fraudster_event','fraudster','fraudster_att']
        df['fraud'] = df['acct_type'].map(lambda x: 1 if x in fraud_types else 0)
        del df['acct_type']  # This is basically the Y-label.
    else:
        pass

    if 'listed' in df.columns:
        df['listed'] = df['listed'].map(lambda x: 1 if x == 'y' else 0)
    else:
        pass

    if 'venue_address' in df.columns:
        df['venue_address_missing'] = pd.isnull(df.venue_address).apply(int)
        del df['venue_address']
    else:
        pass
    
    if 'venue_name' in df.columns:
        df['venue_name_missing'] = pd.isnull(df.venue_name).apply(int)
        del df['venue_name']
    else:
        pass
    
    if 'venue_state' in df.columns:
        df['venue_state_missing'] = pd.isnull(df.venue_state).apply(int)
        del df['venue_state']   # 443 unique values, so probably too many for dummy vars.
    else:
        pass

    
    kill_blanks = ['has_header',
                  'venue_latitude',
                  'venue_longitude']
    
    for c in kill_blanks:
        if c in df.columns:
            df[c][pd.isnull(df[c])] = 0
        else:
            pass

    if 'org_facebook' in df.columns:
        df['org_facebook'][pd.isnull(df['org_facebook'])] = 9999
    else:
        pass

    if 'org_twitter' in df.columns:
        df['org_twitter'][pd.isnull(df['org_twitter'])] = 9999
    else:
        pass

    if 'sale_duration' in df.columns:
        if 'sale_duration2' in df.columns:
            df['sale_duration'][pd.isnull(df['sale_duration'])] = df['sale_duration2']
        else:
            df['sale_duration'][pd.isnull(df['sale_duration'])] = 0
    else:
        pass

     
    # These columns we want to make into dummies:
    dum_columns = ['channels',
                   'country',
                   'venue_country', 
                   'currency', 
                   'delivery_method', 
                   'payout_type', 
                   'user_type']

    for c in dum_columns:
        if c in df.columns:
            df = pd.get_dummies(df, columns=[c], dummy_na=True)
        else:
            pass
 
    # These columns we want to delete, primarily because they are non-numeric:
    del_columns = ['description',
                   'email_domain',
                   'name',
                   'object_id',
                   'org_desc',
                   'org_name',
                   'payee_name',
                   'previous_payouts',
                   'ticket_types']

    for c in del_columns:
        if c in df.columns:
            del df[c]
        else:
            pass
    

    # DateTime columns; we think these are in Unix format (seconds from January 1, 1970, 0:00:00).
    # These might have value in a relative sense, but probably not so much in the absolute.

    datetime_columns = ['user_created',
                       'event_created',
                       'event_published',
                       'event_start',
                       'event_end',
                       'approx_payout_date']

    for c in datetime_columns:
        if c in df.columns:
            df[c][pd.isnull(df[c])] = 0
        else:
            pass


    if 'user_created' in df.columns:
        if 'approx_payout_date' in df.columns:
            df['payout_minus_usercreated'] = df['approx_payout_date'] - df['user_created']
        else:
            pass
        
        if 'event_end' in df.columns:
            df['eventend_minus_usercreated'] = df['event_end'] - df['user_created']
        else:
            pass
        
        if 'event_start' in df.columns:
            df['eventstart_minus_usercreated'] = df['event_start'] - df['user_created']
        else:
            pass
        
        if 'event_published' in df.columns:
            df['eventpublish_minus_usercreated'] = df['event_published'] - df['user_created']
        else:
            pass
        
        if 'event_created' in df.columns:
            df['eventcreated_minus_usercreated'] = df['event_created'] - df['user_created']
        else:
            pass
    else:
        pass
    
    if 'event_created' in df.columns:
        if 'approx_payout_date' in df.columns:
            df['payout_minus_eventcreated'] = df['approx_payout_date'] - df['event_created']
        else:
            pass
        
        if 'event_end' in df.columns:
            df['eventend_minus_eventcreated'] = df['event_end'] - df['event_created']
        else:
            pass
        
        if 'event_start' in df.columns:
            df['eventstart_minus_eventcreated'] = df['event_start'] - df['event_created']
        else:
            pass
            
        if 'event_published' in df.columns:
            df['eventpublish_minus_eventcreated'] = df['event_published'] - df['event_created']
        else:
            pass
        
    if 'event_published' in df.columns:
        if 'approx_payout_date' in df.columns:
            df['payout_minus_eventpublished'] = df['approx_payout_date'] - df['event_published']
        else:
            pass

        if 'event_end' in df.columns:
            df['eventend_minus_eventpublished'] = df['event_end'] - df['event_published']
        else:
            pass
        
        if 'event_start' in df.columns:
            df['eventstart_minus_eventpublished'] = df['event_start'] - df['event_published']
        else:
            pass

    else:
        pass
    
    if 'event_start' in df.columns:
        if 'approx_payout_date' in df.columns:
            df['payout_minus_eventstart'] = df['approx_payout_date'] - df['event_start']
        else:
            pass

        if 'event_end' in df.columns:
            df['eventend_minus_eventstart'] = df['event_end'] - df['event_start']
        else:
            pass

    if 'event_end' in df.columns:
        if 'approx_payout_date' in df.columns:
            df['payout_minus_eventend'] = df['approx_payout_date'] - df['event_end']
        else:
            pass
    else:
        pass


    datetime_columns = ['user_created',
                       'event_created',
                       'event_published',
                       'event_start',
                       'event_end',
                       'approx_payout_date']

    for c in datetime_columns:
        if c in df.columns:
            del df[c]
        else:
            pass

    return df