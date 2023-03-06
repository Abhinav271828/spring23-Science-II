The equations of motion for the system are as follows:
$$\begin{split}
m_1\ddot{y_1} &= -k_1y + k_2(y_2-y_1) + m_1g \\
m_2\ddot{y_2} &= -k_2(y_2-y_1) + k_2(y_3-y_2) \\
m_3\ddot{y_3} &= -k_3(y_3-y_2)
\end{split}$$

These can be written in matrix form as
$$\begin{bmatrix}
-k_1-k_2 & k_2 & 0 \\
k_2 & -k_2-k_3 & k_3 \\
0 & k_2 & -k_3
\end{bmatrix}
\begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix}
=
\begin{bmatrix}
m_1 & 0 & 0 \\
0 & m_2 & 0 \\
0 & 0 & m_3
\end{bmatrix}
\begin{bmatrix}
\ddot{y_1} - g \\
\ddot{y_2} - g \\
\ddot{y_3} - g
\end{bmatrix}$$
