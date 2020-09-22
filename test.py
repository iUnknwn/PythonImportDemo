from testpkg import * #this should import testmod.submod as submod
 
submod.testFunc() # this call works normally, but is flagged by pyright