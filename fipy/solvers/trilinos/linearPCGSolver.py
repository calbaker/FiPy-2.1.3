#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "linearPCGSolver.py"
 #
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #  Author: Maxsim Gibiansky <maxsim.gibiansky@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 # ###################################################################
 ##

__docformat__ = 'restructuredtext'

from fipy.solvers.trilinos.trilinosAztecOOSolver import TrilinosAztecOOSolver
from fipy.solvers.trilinos.preconditioners.multilevelDDPreconditioner import MultilevelDDPreconditioner

from PyTrilinos import AztecOO

class LinearPCGSolver(TrilinosAztecOOSolver):

    """
    The `LinearPCGSolver` is an interface to the cg solver in Trilinos, using
    the `MultilevelSGSPreconditioner` by default.

    """
      
    def __init__(self, tolerance=1e-10, iterations=1000, steps=None, precon=MultilevelDDPreconditioner()):
        """
        :Parameters:
          - `tolerance`: The required error tolerance.
          - `iterations`: The maximum number of iterative steps to perform.
          - `steps`: A deprecated name for `iterations`.
          - `precon`: Preconditioner to use.

        """
        TrilinosAztecOOSolver.__init__(self, tolerance=tolerance,
                                       iterations=iterations, steps=steps, precon=precon)
        self.solver = AztecOO.AZ_cg

    def _canSolveAsymmetric(self):
        return False
                
