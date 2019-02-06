import pandas as pd
from jobs import utilities
from jobs import visualisation


data_frame = pd.read_csv('dataset/data.csv')
series_co_with_p2p = data_frame.loc[(data_frame["p2p"] != 0.0) & (data_frame["connected"] == True)]
series_co_without_p2p = data_frame.loc[((data_frame["p2p"] == 0.0) & (data_frame["connected"] == True))]
series_no_co_without_p2p = data_frame.loc[(data_frame["p2p"] == 0.0) & (data_frame["connected"] == False)]


utilities.pie_media_presence(series_co_with_p2p, 'isp', 'connected and p2p')
utilities.pie_media_presence(series_co_with_p2p, 'browser', 'connected and p2p')
utilities.pie_media_presence(series_co_with_p2p, '#stream', 'connected and p2p')
utilities.pie_media_presence(series_co_without_p2p, 'isp', 'connected without p2p')
utilities.pie_media_presence(series_co_without_p2p, 'browser', 'connected without p2p')
utilities.pie_media_presence(series_co_without_p2p, '#stream', 'connected without p2p')
utilities.pie_media_presence(series_no_co_without_p2p, 'isp', 'unconnected and no p2p')
utilities.pie_media_presence(series_no_co_without_p2p, 'browser', 'unconnected and no p2p')
utilities.pie_media_presence(series_no_co_without_p2p, '#stream', 'unconnected and no p2p')
utilities.connected_unconnected_p2p(series_co_with_p2p, series_co_without_p2p, series_no_co_without_p2p)
visualisation.plot_bargraph_with_groupings(data_frame, 'browser', 'Most used browser', 'browser', 'Frequency')
visualisation.plot_bargraph_with_groupings(data_frame, 'isp', 'Most used isp', 'browser', 'Frequency')
visualisation.plot_bargraph_with_groupings(data_frame, '#stream', 'Most watched stream', 'browser', 'Frequency')
series_stream_is_3 = data_frame.loc[data_frame["#stream"] == 3]
utilities.pie_media_presence(data_frame, series_stream_is_3, 'browser', 'stream ID 3')
utilities.pie_media_presence(data_frame, series_stream_is_3, 'isp', 'stream ID 3')

