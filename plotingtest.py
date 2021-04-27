import pandas as pd
import pandas as pd
df_OLD = pd.read_excel("metoile1.csv").fillna(0)
df_NEW = pd.read_excel("bestgenerated.csv").fillna(0)

dfDiff = df_OLD.copy()
for row in range(dfDiff.shape[0]):
    for col in range(dfDiff.shape[1]):
        value_OLD = df_OLD.iloc[row,col]
        try:
            value_NEW = df_NEW.iloc[row,col]
            if value_OLD==value_NEW:
                dfDiff.iloc[row,col] = df_NEW.iloc[row,col]
            else:
                dfDiff.iloc[row,col] = ('{}-->{}').format(value_OLD,value_NEW)
        except:
            dfDiff.iloc[row,col] = ('{}-->{}').format(value_OLD, 'NaN')


writer = pd.ExcelWriter(fname, engine='xlsxwriter')

dfDiff.to_excel(writer, sheet_name='DIFF', index=False)
df_NEW.to_excel(writer, sheet_name=path_NEW.stem, index=False)
df_OLD.to_excel(writer, sheet_name=path_OLD.stem, index=False)

workbook  = writer.book
worksheet = writer.sheets['DIFF']
worksheet.hide_gridlines(2)

# define formats
grey_fmt = workbook.add_format({'font_color': '#E0E0E0'})
highlight_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})

## highlight changed cells
worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                        'criteria': 'containing',
                                        'value':'→',
                                        'format': highlight_fmt})
## highlight unchanged cells
worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                        'criteria': 'not containing',
                                        'value':'→',
                                        'format': grey_fmt})
# save
writer.save()