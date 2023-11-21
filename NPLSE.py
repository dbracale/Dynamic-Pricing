{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f4999e0a-3f58-403b-8a1a-784e43480da6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from scipy.optimize import minimize, NonlinearConstraint\n",
    "from scipy.interpolate import interp1d\n",
    "\n",
    "def objective_function(alpha, y_s):\n",
    "    return np.sum((y_s + 1/alpha)**2)\n",
    "\n",
    "def constraint(alpha, epsi):\n",
    "    return np.concatenate([\n",
    "        -1/epsi - alpha,\n",
    "        1/(1 - epsi) + alpha,\n",
    "        np.diff(alpha),\n",
    "        np.diff(np.diff(alpha))\n",
    "    ])\n",
    "\n",
    "def LS(w, y, epsi):\n",
    "    w_unique = np.unique(w)\n",
    "    n = len(w_unique)\n",
    "    w_sorted = np.sort(w_unique)\n",
    "    index = np.argsort(w)\n",
    "\n",
    "    y_s = [y[i] for i in index]\n",
    "    y_s = np.array(y_s, dtype=int)\n",
    "\n",
    "    # Initial guess for alpha\n",
    "    alpha0 = -np.ones(n)\n",
    "\n",
    "    # Define the objective and constraints for scipy.optimize\n",
    "    obj_func = lambda alpha: objective_function(alpha, y_s)\n",
    "    nonlinear_constraint = NonlinearConstraint(lambda alpha: constraint(alpha, epsi), -np.inf, 0)\n",
    "\n",
    "    # Minimize the objective function subject to constraints\n",
    "    result = minimize(obj_func, alpha0, constraints=[nonlinear_constraint])\n",
    "\n",
    "    phi = result.x\n",
    "    F_hat = interp1d(w_sorted, 1+1/phi, kind='linear', fill_value='extrapolate')\n",
    "    return F_hat\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
