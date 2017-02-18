from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

def show_confusion_matrix(y_true, y_predict, truelabel='True', falselabel='False'):
    CM = confusion_matrix(y_true, y_predict)
    tp = CM[1,1]
    fp = CM[0,1]
    fn = CM[1,0]
    tn = CM[0,0]
    total = tp+tn+fp+fn

    # Re-arranges the confusion matrix to conventional format.
    newCM = np.array([[tp, fp], [fn, tn]])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(newCM)
    plt.title('Confusion Matrix')
    fig.colorbar(cax)
    ax.set_xticklabels(['']+[truelabel, falselabel])
    ax.set_yticklabels(['']+[truelabel, falselabel])
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.show()

    print "True Positive:", tp, "or", np.around(100*float(tp)/total,2), "%"
    print "True Negative:", tn, "or", np.around(100*float(tn)/total,2), "%"
    print "False Positive:", fp, "or", np.around(100*float(fp)/total,2), "%"
    print "False Negative:", fn, "or", np.around(100*float(fn)/total,2), "%"
    print "Total", total
    print "Total Wrong:", fp+fn, "or", np.around(100*float(fp+fn)/total,2), "%"
    print '\n'
    print "Accuracy:", np.around((tp+tn)/float(total),4)
    print "Precision (Positive Predictive Value):", np.around(tp/float(tp+fp),4)
    print "Negative Predictive Value:",np.around(tn/float(tn+fn),4)
    print "Recall (True Positive Rate):", np.around(tp/float(tp+fn),4)
    print "Specificity (True Negative Rate):", np.around(tn/float(tn+fp),4)