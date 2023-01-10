def digital_root(n):
    # ...
    while(n>9):
        res=0
        while(n):
            res+=n%10
            n//=10
        n=res
    return(n)
  
  
  # Another method
  
  def digital_root(n):
    # ...
    while(n>9):
        n=sum(int(i) for i in str(n))
    return n 
  
  @test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)
