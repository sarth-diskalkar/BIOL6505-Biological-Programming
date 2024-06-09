"""Adapted from code developed in BIOL6750, Fall 2021, Prof. Joshua Weitz"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
totsteps = 1000
delt = 1
v0 = 0.3


def boids_dyn(pars):
    '''
    function [xt,yt,thetat]=boids_dyn(N,L,eta)
    inputs:
    N--number of boids, L--linear dimension of domain, eta--strength of noise
    outputs
    xt and yt -- positions of each boid over time
    thetat -- direction of velocity of each boid over time
    '''
    L = pars['L']
    N = pars['N']
    eta = pars['eta']
    R = pars['R']
    currx = L*np.random.uniform(size=N)
    curry = L*np.random.uniform(size=N)
    currtheta = 2*np.pi*np.random.uniform(size=N)
    xt = np.zeros((totsteps, N))
    yt = np.zeros((totsteps, N))
    thetat = np.zeros((totsteps, N))
    for t in range(totsteps):
        for i in range(N):
            x_dists = currx-currx[i]
            x_dists[x_dists > L/2] = L - x_dists[x_dists > L/2]
            y_dists = curry-curry[i]
            y_dists[y_dists > L/2] = L - y_dists[y_dists > L/2]
            dists = np.linalg.norm(np.vstack((x_dists, y_dists)), axis=0)
            neighbors = np.nonzero((dists <= R) & (dists >= 0))
            sin_avg = np.mean(np.sin(currtheta[neighbors]))
            cos_avg = np.mean(np.cos(currtheta[neighbors]))
            theta_new = np.arctan(sin_avg/cos_avg) + np.pi*np.heaviside(-cos_avg, 1)
            theta_new += np.random.uniform(-eta/2, eta/2)
            thetat[t, i] = theta_new
            xt[t, i] = currx[i] + v0 * delt * np.cos(theta_new)
            if xt[t, i] > L:
                xt[t, i] = xt[t, i] % L
            elif xt[t, i] < 0:
                xt[t, i] = xt[t, i] + L
            yt[t, i] = curry[i] + v0 * delt * np.sin(theta_new)
            if yt[t, i] > L:
                yt[t, i] = yt[t, i] % L
            elif yt[t, i] < 0:
                yt[t, i] = yt[t, i] + L
        currx = xt[t]
        curry = yt[t]
        currtheta = thetat[t]

    return [xt, yt, thetat]

def animated_plot(xt, yt, vxt, vyt, fname):
    print('generating animation. Please wait')
    fig, ax = plt.subplots()

    def update(frame):
        if frame % 10 == 0:
            print('{}/{}'.format(frame, totsteps))
        ax.clear()
        q = ax.quiver(xt[frame], yt[frame], vxt[frame], vyt[frame], color='grey')
        s = ax.scatter(xt[frame], yt[frame], s=4, color='black')
        ax.set(xlim=[0, 30], ylim=[0, 30])
        return q, s
    anim = FuncAnimation(fig, update, frames=totsteps, blit=True, interval=100)
    anim.save('{}.mp4'.format(fname))
    plt.close('all')


def run_sim(L, N, eta, R, fname):
    pars = {'L': L, 'N': N, 'eta': eta, 'R': R}
    xt, yt, thetat = boids_dyn(pars)
    vxt = v0 * np.cos(thetat)
    vyt = v0 * np.sin(thetat)
    animated_plot(xt, yt, vxt, vyt, fname)