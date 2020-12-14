from reunion.trends import ReunionTrends

if __name__ == '__main__':
    trends = ReunionTrends()
    print(trends.get_popularities())
    trends.save_to_db()


