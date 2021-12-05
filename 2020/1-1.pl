open my $handle, '<', "input.txt";
chomp(my @input = <$handle>);
close $handle;

foreach(@input) {
  $x = $_; 
  foreach (@input) {
    $y = $_;
    foreach (@input) {
      $z = $_;
      #print ("z = " . $z . "\n");
      if ($x + $y + $z  == 2020) {
        print("x = " . $x . ", y = " . $y . ", z = " . $z . ".\n");
        print("x * y * z = " . $x * $y * $z  . ".");
      }
    }
  }
}

