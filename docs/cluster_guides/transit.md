# Transit

[Transit](../cluster_guides/transit.md)
is an UPPMAX service that can be used to securely transfer files.

???- question "Is Transit a file server?"

    Transit is a service, not a file server.
    Transit is not a file server, as it does not store files.

    This can be observed by uploading files to Transit
    and then closing this connection
    before sending the files to a permanent location:
    the Transit-only files will disappear.

???- question "What is Transit?"

    ![From https://sv.wikipedia.org/wiki/Brevl%C3%A5da#/media/Fil:Brevl%C3%A5dor.jpg](./img/swedish_postbox_117_x_157.jpg)

    > A Swedish post box. The yellow post box is for non-regional mail,
    > the blue for regional mail.

    Transit can be viewed as [a post box](https://en.wikipedia.org/wiki/Post_box),
    where the file you upload is a letter.

    If you put a letter without an address in a post box,
    it will be thrown away.

    If you put an address on the letter,
    the letter will be delivered.
    Here, 'putting an address on the letter'
    is to copy the file to the desired location.

 * [how to log in to Transit](../cluster_guides/login_transit.md)
 * [file transfer using Transit](../cluster_guides/transfer_transit.md).
 * [software on Transit](../cluster_guides/software_on_transit.md)
