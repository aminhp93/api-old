import requests
import logging
import datetime
from stock_schedule_manager.models import StockScheduleManager
import json

LIST_ALL_STYMBOLS = ['HPG','HSG','NKG','SHI','SMC','TLH','ABB','ACB','BID','BVB','CTG','HDB','KLB','LPB','MBB','MSB','NAB','NVB','OCB','PGB','SHB','STB','TCB','TPB','VIB','VPB','EIB','SGB','SSB','VBB','VCB','AGG','D2D','DIG','DXG','HDC','HDG','HPX','IJC','KDH','LHG','NLG','NTL','NVL','PDR','SJS','TDC','TIG','TIP','KBC','SCR','KHG','CRE','HQC','CKG','AGR','BSI','BVS','CTS','FTS','HCM','MBS','ORS','SHS','SSI','TVB','VCI','VIX','VND','VDS','SBS','BSR','OIL','PLX','PVD','PVS','PVC','ADS','DLG','APG','PAS','TCD','DRC','OGC','DDG','AMV','FIT','MST','HAX','DPR','VGS','IPA','MBG','HHS','ITC','BCM','LDG','GEG','LCG','EVG','AAT','KOS','VC3','HVN','TTF','DDV','PTB','PET','DXS','CSV','FIR','NT2','NBB','DPG','SAM','VGI','SSH','MIG','ABS','FCN','CTF','C4G','KSB','IDI','PNJ','TCM','GMD','CTR','SCG','CTD','SZC','DHC','HBC','VPI','VJC','BCG','VPG','HUT','APH','ANV','REE','HNG','VGC','VHC','HHV','PHR','TNG','AAA','CEO','GAS','PVT','HAH','GVR','BVH','BAF','PC1','GIL','ASM','PAN','SBT','DGW','DBC','FRT','TCH','VRE','DPM','FPT','CII','VCG','DCM','POW','IDC','HAG','MWG','GEX','DGC','HT1','BCC']
TABLE_NAME = 'stock'
# TABLE_NAME = 'stock_test'

def daily_import_stock_job(date=None):
    try:
        # get current date in string format
        if date:
            request_date = date
        else:
            now = datetime.datetime.now()
            request_date = now.strftime("%Y-%m-%d")

        real_request_date = request_date
        
        data = []
        for i in LIST_ALL_STYMBOLS:
            print('start request:  ' + i)
            url_1 = "https://restv2.fireant.vn/symbols/" + i + "/historical-quotes?startDate=2022-01-01&endDate=" + request_date + "&offset=0&limit=20"
            
            headers_1 = {
                'accept': 'application/json, text/plain, */*',
                'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxOTEzNjIzMDMyLCJuYmYiOjE2MTM2MjMwMzIsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsInJvbGVzIiwiZW1haWwiLCJhY2NvdW50cy1yZWFkIiwiYWNjb3VudHMtd3JpdGUiLCJvcmRlcnMtcmVhZCIsIm9yZGVycy13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImZpbmFuY2UtcmVhZCIsInBvc3RzLXdyaXRlIiwicG9zdHMtcmVhZCIsInN5bWJvbHMtcmVhZCIsInVzZXItZGF0YS1yZWFkIiwidXNlci1kYXRhLXdyaXRlIiwidXNlcnMtcmVhZCIsInNlYXJjaCIsImFjYWRlbXktcmVhZCIsImFjYWRlbXktd3JpdGUiLCJibG9nLXJlYWQiLCJpbnZlc3RvcGVkaWEtcmVhZCJdLCJzdWIiOiIxZmI5NjI3Yy1lZDZjLTQwNGUtYjE2NS0xZjgzZTkwM2M1MmQiLCJhdXRoX3RpbWUiOjE2MTM2MjMwMzIsImlkcCI6IkZhY2Vib29rIiwibmFtZSI6Im1pbmhwbi5vcmcuZWMxQGdtYWlsLmNvbSIsInNlY3VyaXR5X3N0YW1wIjoiODIzMzcwOGUtYjFjOS00ZmQ3LTkwYmYtMzI2NTYzYmU4N2JkIiwianRpIjoiZmIyZWJkNzAzNTBiMDBjMGJhMWE5ZDA5NGUwNDMxMjYiLCJhbXIiOlsiZXh0ZXJuYWwiXX0.OhgGCRCsL8HVXSueC31wVLUhwWWPkOu-yKTZkt3jhdrK3MMA1yJroj0Y73odY9XSLZ3dA4hUTierF0LxcHgQ-pf3UXR5KYU8E7ieThAXnIPibWR8ESFtB0X3l8XYyWSYZNoqoUiV9NGgvG2yg0tQ7lvjM8UYbiI-3vUfWFsMX7XU3TQnhxW8jYS_bEXEz7Fvd_wQbjmnUhQZuIVJmyO0tFd7TGaVipqDbRdry3iJRDKETIAMNIQx9miHLHGvEqVD5BsadOP4l8M8zgVX_SEZJuYq6zWOtVhlq3uink7VvnbZ7tFahZ4Ty4z8ev5QbUU846OZPQyMlEnu_TpQNpI1hg',
            }
            
            response_get_fireant = requests.request("GET", url_1, headers=headers_1)
            response_get_fireant.raise_for_status()

            data_payload = response_get_fireant.json()[0]
            data_payload['key'] = data_payload['symbol'] + "_" + data_payload['date']

            # replace T00:00:00 to empty
            data_payload['date'] = data_payload['date'].replace('T00:00:00', '')
            
            data.append(data_payload)
            real_request_date = data_payload['date']
            print('end request:  ' + data_payload['key'])

        print('start superbase')

        headers = {
            'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuaW1hd3NvdWVocGtiaXBxcXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzM0NDY4MzcsImV4cCI6MTk4OTAyMjgzN30.K_BGIC_TlWbHl07XX94EWxRI_2Om_NKu_PY5pGtG-hk',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuaW1hd3NvdWVocGtiaXBxcXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzM0NDY4MzcsImV4cCI6MTk4OTAyMjgzN30.K_BGIC_TlWbHl07XX94EWxRI_2Om_NKu_PY5pGtG-hk',
            'Content-Type': 'application/json',
            'Prefer': 'return=minimal'
        }

        print("start delete")
        # DELETE ALL DATA OF THAT DATE BEFORE IMSERT
        url_delete = "https://bnimawsouehpkbipqqvl.supabase.co/rest/v1/" + TABLE_NAME + "?date=eq." + real_request_date
        response_delete = requests.request("DELETE", url_delete, headers=headers)
        response_delete.raise_for_status()

        print("DONE delete")

        print("start insert")
        url_insert = "https://bnimawsouehpkbipqqvl.supabase.co/rest/v1/" + TABLE_NAME
        payload_insert = json.dumps(data)
        response_insert = requests.request("POST", url_insert, headers=headers, data=payload_insert)
        response_insert.raise_for_status()

        print("DONE insert")

        print('end superbase')
        StockScheduleManager.objects.filter(date=real_request_date).delete()
        StockScheduleManager.objects.create(
            date=real_request_date,
            status=True
        )
        
        print('DONE')
        return "DONE"
    except Exception as e:
        print('ERROR', e)
        StockScheduleManager.objects.filter(date=real_request_date).delete()
        StockScheduleManager.objects.create(
            date=real_request_date,
            status=False
        )
        return "ERROR"
            



