document$.subscribe(function() {
    var tableElement = $('.sortable_searchable_table table');
    
    // ====== CONFIG: Define columns and their settings ======
    var columnSettings = [
        { name: 'Versions', maxWidth: '120px', truncate: null },
//        { name: 'Module', maxWidth: '150px', truncate: 20 },
//        { name: 'Name', maxWidth: '180px', truncate: null }  // null = no truncation
    ];
    // =======================================================
    
    var dtConfig = {
        pageLength: 50, 
        searching: true,
        ordering: true,
        destroy: true,
        paging: false,
        columnDefs: []
    };
   
    // Build columnDefs for each configured column
    tableElement.find('thead th').each(function(index) {
        var headerText = $(this).text().trim();
        var settings = columnSettings.find(s => s.name === headerText);
        
        if (settings) {
            dtConfig.columnDefs.push({
                targets: index,
                createdCell: function(td, cellData, rowData, row, col) {
                    $(td).css({
                        'max-width': settings.maxWidth,
                        'word-wrap': 'break-word',
                        'white-space': 'normal',
                        'overflow-wrap': 'break-word'
                    });
                }
            });
        }
    });
    
    tableElement.DataTable(dtConfig);
});

