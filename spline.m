clear all
close all

p0=[0,0]
p1=[1.5,0.2]%[1.5,.2]
p2=[1.5,-1.7]
t=[0:0.1:1]
figure(1)
plot(p0(1),p0(2),'*')
hold on
plot(p1(1),p1(2),'*')
plot(p2(1),p2(2),'*')
[a,b]=size(t)
R=zeros(100,2)
ciclo=20
c=1/ciclo
for i=1:ciclo
   %Q0=(1-t(i))*p0+t(i)*p1
   %Q0=p0-p0*t(i)+t(i)*p1
   Q0=p0-p0*i*c+i*c*p1
   %Q1=(1-t(i))*p1+t(i)*p2
   %Q1=p1-p1*t(i)+t(i)*p2
   Q1=p1-p1*i*c+i*c*p2
   %R=(1-t(i))*Q0+t(i)*Q1
   %R=Q0-Q0*t(i)+t(i)*Q1
   R=Q0-Q0*i*c+i*c*Q1
   hold on
   plot(R(1),R(2),'*')
end





%for j=3:5
 p0=[0.5,-0.5]
%p1=[1.5,0.2]%[1.5,.2]
p1=[1.5,-1.7]
p2=[1.99,-1.7]
t=[0:0.1:1]
 
figure(3)
plot(p0(1),p0(2),'*')
hold on
plot(p1(1),p1(2),'*')
plot(p2(1),p2(2),'*')
[a,b]=size(t)
R=zeros(100,2)
ciclo=20
c=1/ciclo

%figure(j+15)
    for i=1:ciclo
        %Q0=(1-t(i))*p0+t(i)*p1
        %Q0=p0-p0*t(i)+t(i)*p1
        Q0=p0-p0*i*c+i*c*p1
        %Q1=(1-t(i))*p1+t(i)*p2
        %Q1=p1-p1*t(i)+t(i)*p2
        Q1=p1-p1*i*c+i*c*p2
   %R=(1-t(i))*Q0+t(i)*Q1
   %R=Q0-Q0*t(i)+t(i)*Q1
        R=Q0-Q0*i*c+i*c*Q1
        hold on
        plot(R(1),R(2),'*')
    end
%end

drawArrow = @(x,y,varargin) quiver( x(1),y(1),x(2)-x(1),y(2)-y(1),0, varargin{:} )       
%drawArrow(p1,p0); hold on
%drawArrow(p1,p2,'linewidth',3,'color','r')
%drawArrow(p0,p1,'linewidth',3,'color','r')