FROM continuumio/miniconda3
RUN chmod a+rw /root/.conda/environments.txt
RUN conda update conda -c anaconda