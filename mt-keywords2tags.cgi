#!/usr/bin/perl -w
#
# $Id$
# A simple tool for converting entries' keywords into tags for MT 3.3+
#
# This software is provided as-is. You may use it for commercial or 
# personal use. If you distribute it, please keep this notice intact.
#
# Copyright (c) 2006 Hirotaka Ogawa
#
use strict;
sub BEGIN {
    my $dir;
    require File::Spec;
    if (!($dir = $ENV{MT_HOME})) {
        if ($0 =~ m!(.*[/\\])!) {
            $dir = $1;
        } else {
            $dir = './';
        }
        $ENV{MT_HOME} = $dir;
    }
    unshift @INC, File::Spec->catdir($dir, 'lib');
    unshift @INC, File::Spec->catdir($dir, 'extlib');
}

$| = 1;
print "Content-Type: text/html\n\n";
print <<HTML;
<html>
<head><title>mt-keywords2tags</title></head>
<body>
<h1>mt-keywords2tags</h1>

<pre>
HTML

use MT;
use MT::Entry;

my $mt = MT->new or die MT->errstr;
my $iter = MT::Entry->load_iter;

while (my $e = $iter->()) {
    next unless $e->keywords;
    my @tags = split_tags($e->keywords, 1);
    next unless scalar @tags;
    $e->set_tags(@tags);
    $e->save_tags;
    print $e->id . ": " . join(', ', @tags) . "\n";
}

print <<HTML;
</pre>
<p><strong>Successfully added tags.</strong></p>
</body>
</html>
HTML

sub split_tags {
    my ($string, $case_sensitive) = @_;
    return unless $string;
    my @tags;
    $string =~ s/\#.*$//g;
    $string =~ s/(^\s+|\s+$)//g;
    $string = lc $string unless $case_sensitive;
#    $string =~ s/\[[^[]+\]//g; # uncomment this to discard [short title]

    if ($string =~ m/[;,|]/) {
	# tags separated by non-whitespaces
	while ($string =~ m/(\[[^]]+\]|"[^"]+"|'[^']+'|[^;,|]+)/g) {
	    my $tag = $1;
	    $tag =~ s/(^[\["'\s;,|]+|[\]"'\s;,|]+$)//g;
	    push @tags, $tag if $tag;
	}
    } else {
	# tags separated by whitespaces
	while ($string =~ m/(\[[^]]+\]|"[^"]+"|'[^']+'|[^\s]+)/g) {
	    my $tag = $1;
	    $tag =~ s/(^[\["'\s]+|[\]"'\s]+$)//g;
	    push @tags, $tag if $tag;
	}
    }
    @tags;
}
