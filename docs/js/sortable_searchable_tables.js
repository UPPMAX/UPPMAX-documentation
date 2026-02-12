document$.subscribe(function() {
    $('.sortable_searchable_table table').DataTable({
        pageLength: 50,
        searching: true,
        ordering: true,
        destroy: true,  // Important for page reloads in MkDocs
        paging: false
    });
});

