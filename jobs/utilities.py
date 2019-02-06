from jobs import visualisation


def generate_comparison_visualisation(sorted_list, title):
    labels = tuple([str(i[0]) for i in sorted_list])
    data = [int(i[1]) for i in sorted_list]
    explode = ([0.1] + [0] * (len(data) - 1))

    visualisation.generate_pie(data, labels, title, explode)


def connected_unconnected_p2p(series_co_with_p2p, series_co_without_p2p, series_no_co_without_p2p):
    total = (len(series_co_without_p2p) + len(series_no_co_without_p2p) + len(series_co_with_p2p)) / 100
    visualisation.generate_pie([len(series_co_with_p2p)/total, len(series_co_without_p2p)/total,
                                len(series_no_co_without_p2p)/total], ('p2p & co', 'co without p2p', 'not co'),
                               'comparison between configuration p2p')


def pie_media_presence(series_df, colum_name, title):
    series_df_counts = series_df[colum_name].value_counts()
    percentage = dict()
    for key, value in series_df_counts.iteritems():
        percentage.update({key: round(value / len(series_df) * 100, ndigits=2)})
    percentage = sorted(percentage.items(), key=lambda kv: kv[1], reverse=True)
    generate_comparison_visualisation(percentage, '{} presence for {}'.format(colum_name, title))


def pie_using_p2p(series_df, title):
    total = len(series_df)
    p = len(series_df.loc[series_df['p2p'] != 0.0])/total*100
    visualisation.generate_pie([p, 100 - p],
                               ('Is using p2p', "Isn't using p2p"), 'p2p usecase for : {}'.format(title))
