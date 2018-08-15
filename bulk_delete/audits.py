import customer_search.actions  # Don't like this, move it


def verify_bulk_delete(old_count):
    new_count = customer_search.actions.get_search_results_count()

    assert new_count != old_count, 'Incorrect customer count found. Expected count to be something other than {}'\
        .format(old_count)
