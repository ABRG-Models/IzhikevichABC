def plot_izhi (title, v, u, Vn, nc_v, nc_u, Vg, ug, vdot, udot,
               qvlowerv, qvupperv, qvloweru, qvupperu, qpspacing, qpveclen):

    #%matplotlib inline
    import matplotlib.pyplot as plt
    import numpy as np
    
    plt.figure(figsize=(18,10))
    plt.clf;        
    
    # Plot vector field
    if qpspacing != 0:
        # Note arbitrary scaling of udot by factor of 10 here:
        Q = plt.quiver(Vg, ug, vdot, udot*10, pivot='mid', color='k', width=0.001, scale=qpveclen)
        lef,rgt,bot,top = plt.axis()
        plt.axis([lef, rgt, bot, top])
    else:
        plt.axis([qvlowerv, qvupperv, qvloweru, qvupperu])

    #print len(nc_v)
    if len(nc_v) < 100:
        # In this case assume it's an array of arrays
        for nc_v_i in nc_v:
            #print 'length',len(nc_v_i)
            #print 'first value',nc_v_i[0]
            plt.plot(Vn, nc_v_i)
    else:
        plt.plot(Vn, nc_v)
    
    plt.plot(Vn, nc_u, color='r')

    plt.title(title)
    plt.xlabel('v');
    plt.ylabel('u');

    plt.plot(v, u, color='g')

    # To put coloured points on the graph for path debugging:
    debug_path = False
    if debug_path:
        vlen = len(v)
        pts = np.linspace(0,vlen-1,100)
        import time
        for point in pts:
            p=int(point)
            plt.plot(v[p],u[p],marker='o')
